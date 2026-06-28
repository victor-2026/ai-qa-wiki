package analyzer

import (
	"encoding/csv"
	"fmt"
	"io"
	"math"
	"sort"
	"strconv"
	"strings"
	"time"
)

type Post struct {
	Date        time.Time
	Topic       string
	Format      string // post, article, carousel, report
	Impressions int
	Likes       int
	Comments    int
	Saves       int
	Shares      int
	Notes       string
	URL         string
	Hashtags    []string
	Engagement  float64 // likes + comments + saves + shares / impressions
}

type Analyzer struct {
	Posts []Post
}

func ParseCSV(r io.Reader) (*Analyzer, error) {
	reader := csv.NewReader(r)
	reader.FieldsPerRecord = -1 // allow variable field count

	// read header
	header, err := reader.Read()
	if err != nil {
		return nil, fmt.Errorf("read header: %w", err)
	}
	if len(header) < 12 {
		return nil, fmt.Errorf("csv has only %d columns, expected 12", len(header))
	}

	a := &Analyzer{}
	for {
		row, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			continue // skip malformed rows
		}
		if len(row) < 12 {
			continue
		}
		p, err := parseRow(row)
		if err != nil {
			continue // skip malformed rows
		}
		a.Posts = append(a.Posts, p)
	}
	return a, nil
}

func parseRow(row []string) (Post, error) {
	p := Post{}

	date, err := time.Parse("2006-01-02", strings.TrimSpace(row[0]))
	if err != nil {
		return p, err
	}
	p.Date = date
	p.Topic = row[1]
	p.Format = row[2]
	p.Impressions = parseInt(row[3])
	p.Likes = parseInt(row[4])
	p.Comments = parseInt(row[5])
	p.Saves = parseInt(row[6])
	p.Shares = parseInt(row[7])
	p.Notes = row[9]
	p.URL = row[10]
	p.Hashtags = parseHashtags(row[11])

	if p.Impressions > 0 {
		p.Engagement = float64(p.Likes+p.Comments+p.Saves+p.Shares) / float64(p.Impressions)
	}
	return p, nil
}

func parseInt(s string) int {
	s = strings.TrimSpace(s)
	if s == "" || s == "?" {
		return 0
	}
	v, err := strconv.Atoi(s)
	if err != nil {
		return 0
	}
	return v
}

func parseHashtags(s string) []string {
	s = strings.TrimSpace(s)
	if s == "" || s == "?" {
		return nil
	}
	tags := strings.Split(s, " ")
	clean := make([]string, 0, len(tags))
	for _, t := range tags {
		t = strings.TrimSpace(t)
		if t != "" {
			clean = append(clean, t)
		}
	}
	return clean
}

// ============================================================
// Level 1: PBT — Data invariants
// ============================================================

func (a *Analyzer) CheckInvariants() []string {
	var violations []string
	for i, p := range a.Posts {
		if p.Impressions < 0 {
			violations = append(violations, fmt.Sprintf("row %d: negative impressions %d", i, p.Impressions))
		}
		if p.Date.After(time.Now()) {
			violations = append(violations, fmt.Sprintf("row %d: future date %s", i, p.Date.Format("2006-01-02")))
		}
		if p.Engagement < 0 || p.Engagement > 1 {
			violations = append(violations, fmt.Sprintf("row %d: engagement rate out of bounds: %.4f", i, p.Engagement))
		}
	}
	return violations
}

// ============================================================
// Level 2: Hashtag analysis (A/B-like comparison)
// ============================================================

type HashtagStat struct {
	Tag          string
	Count        int
	AvgImpressions float64
	AvgEngagement  float64
	BestImpression int
}

func (a *Analyzer) HashtagStats() []HashtagStat {
	tagMap := make(map[string]*HashtagStat)
	for _, p := range a.Posts {
		if len(p.Hashtags) == 0 {
			continue
		}
		for _, tag := range p.Hashtags {
			if !strings.HasPrefix(tag, "#") {
				continue // skip non-hashtag entries (data quality)
			}
			if _, ok := tagMap[tag]; !ok {
				tagMap[tag] = &HashtagStat{Tag: tag}
			}
			s := tagMap[tag]
			s.Count++
			s.AvgImpressions += float64(p.Impressions)
			s.AvgEngagement += p.Engagement
			if p.Impressions > s.BestImpression {
				s.BestImpression = p.Impressions
			}
		}
	}

	result := make([]HashtagStat, 0, len(tagMap))
	for _, s := range tagMap {
		if s.Count > 0 {
			s.AvgImpressions /= float64(s.Count)
			s.AvgEngagement /= float64(s.Count)
		}
		result = append(result, *s)
	}
	sort.Slice(result, func(i, j int) bool {
		return result[i].AvgImpressions > result[j].AvgImpressions
	})
	return result
}

// Format analysis
type FormatStat struct {
	Format         string
	Count          int
	AvgImpressions float64
	AvgEngagement  float64
}

func (a *Analyzer) FormatStats() []FormatStat {
	formatMap := make(map[string]*FormatStat)
	for _, p := range a.Posts {
		if _, ok := formatMap[p.Format]; !ok {
			formatMap[p.Format] = &FormatStat{Format: p.Format}
		}
		s := formatMap[p.Format]
		s.Count++
		s.AvgImpressions += float64(p.Impressions)
		s.AvgEngagement += p.Engagement
	}

	result := make([]FormatStat, 0, len(formatMap))
	for _, s := range formatMap {
		if s.Count > 0 {
			s.AvgImpressions /= float64(s.Count)
			s.AvgEngagement /= float64(s.Count)
		}
		result = append(result, *s)
	}
	sort.Slice(result, func(i, j int) bool {
		return result[i].AvgImpressions > result[j].AvgImpressions
	})
	return result
}

// ============================================================
// Level 3: Drift detection — weekly engagement trend
// ============================================================

type WeeklyStat struct {
	Week          string // ISO week
	PostCount     int
	AvgImpressions float64
	AvgEngagement  float64
	TotalImpressions int
}

func (a *Analyzer) WeeklyDrift() []WeeklyStat {
	weekMap := make(map[string]*WeeklyStat)
	for _, p := range a.Posts {
		year, week := p.Date.ISOWeek()
		key := fmt.Sprintf("%d-W%02d", year, week)
		if _, ok := weekMap[key]; !ok {
			weekMap[key] = &WeeklyStat{Week: key}
		}
		s := weekMap[key]
		s.PostCount++
		s.AvgImpressions += float64(p.Impressions)
		s.AvgEngagement += p.Engagement
		s.TotalImpressions += p.Impressions
	}

	result := make([]WeeklyStat, 0, len(weekMap))
	for _, s := range weekMap {
		if s.PostCount > 0 {
			s.AvgImpressions /= float64(s.PostCount)
			s.AvgEngagement /= float64(s.PostCount)
		}
		result = append(result, *s)
	}
	sort.Slice(result, func(i, j int) bool {
		return result[i].Week < result[j].Week
	})
	return result
}

// DetectDrift flags weeks where avg engagement drops below threshold
func (a *Analyzer) DetectDrift(threshold float64) []string {
	weekly := a.WeeklyDrift()
	if len(weekly) < 2 {
		return nil
	}
	// baseline = first 3 weeks or all if fewer
	n := 3
	if len(weekly) < n {
		n = len(weekly)
	}
	var baselineSum float64
	for i := 0; i < n; i++ {
		baselineSum += weekly[i].AvgEngagement
	}
	baseline := baselineSum / float64(n)

	var alerts []string
	for _, w := range weekly {
		if w.AvgEngagement < baseline-threshold && w.PostCount >= 2 {
			alerts = append(alerts, fmt.Sprintf("week %s avg_engagement=%.4f (baseline=%.4f, posts=%d)",
				w.Week, w.AvgEngagement, baseline, w.PostCount))
		}
	}
	return alerts
}

// ============================================================
// Level 4: Golden dataset — top performer benchmarks
// ============================================================

type Benchmark struct {
	AvgImpressions  float64
	AvgEngagement   float64
	TopHashtags     []string
	TopFormats      []string
	ImpressionsP50  float64
	ImpressionsP90  float64
	EngagementP50   float64
}

func (a *Analyzer) Benchmark() Benchmark {
	b := Benchmark{}
	if len(a.Posts) == 0 {
		return b
	}

	// hashtags
	hs := a.HashtagStats()
	if len(hs) > 0 {
		top := 5
		if len(hs) < top {
			top = len(hs)
		}
		for i := 0; i < top; i++ {
			b.TopHashtags = append(b.TopHashtags, hs[i].Tag)
		}
	}

	// formats
	fs := a.FormatStats()
	if len(fs) > 0 {
		top := 3
		if len(fs) < top {
			top = len(fs)
		}
		for i := 0; i < top; i++ {
			b.TopFormats = append(b.TopFormats, fs[i].Format)
		}
	}

	// percentiles
	imps := make([]float64, len(a.Posts))
	engs := make([]float64, len(a.Posts))
	var impSum, engSum float64
	for i, p := range a.Posts {
		imps[i] = float64(p.Impressions)
		engs[i] = p.Engagement
		impSum += imps[i]
		engSum += engs[i]
	}
	b.AvgImpressions = impSum / float64(len(a.Posts))
	b.AvgEngagement = engSum / float64(len(a.Posts))

	sort.Float64s(imps)
	sort.Float64s(engs)
	b.ImpressionsP50 = percentile(imps, 50)
	b.ImpressionsP90 = percentile(imps, 90)
	b.EngagementP50 = percentile(engs, 50)

	return b
}

func percentile(sorted []float64, p float64) float64 {
	if len(sorted) == 0 {
		return 0
	}
	idx := int(math.Ceil(p/100*float64(len(sorted)))) - 1
	if idx < 0 {
		idx = 0
	}
	if idx >= len(sorted) {
		idx = len(sorted) - 1
	}
	return sorted[idx]
}

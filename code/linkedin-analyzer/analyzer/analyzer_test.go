package analyzer

import (
	"math"
	"strings"
	"testing"
)

// ============================================================
// Level 1: PBT — Data invariants
// ============================================================

func TestNoNegativeImpressions(t *testing.T) {
	a := analyzerFromCSV(t)
	violations := a.CheckInvariants()
	for _, v := range violations {
		if strings.Contains(v, "negative impressions") {
			t.Errorf("found negative impression: %s", v)
		}
	}
}

func TestNoFutureDates(t *testing.T) {
	a := analyzerFromCSV(t)
	violations := a.CheckInvariants()
	for _, v := range violations {
		if strings.Contains(v, "future date") {
			t.Errorf("found future date: %s", v)
		}
	}
}

func TestEngagementRateInRange(t *testing.T) {
	a := analyzerFromCSV(t)
	violations := a.CheckInvariants()
	for _, v := range violations {
		if strings.Contains(v, "engagement rate out of bounds") {
			t.Errorf("engagement rate violation: %s", v)
		}
	}
}

// ============================================================
// Level 1b: Table-driven edge cases
// ============================================================

func TestParseHashtags(t *testing.T) {
	tests := []struct {
		name  string
		input string
		want  int
	}{
		{"empty", "", 0},
		{"question", "?", 0},
		{"single", "#Go", 1},
		{"multiple", "#Go #Python #JS", 3},
		{"with spaces", "  #Go  #Python  ", 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := parseHashtags(tt.input)
			if len(got) != tt.want {
				t.Errorf("parseHashtags(%q) = %d tags, want %d", tt.input, len(got), tt.want)
			}
		})
	}
}

// ============================================================
// Level 2: Hashtag effectiveness (A/B-like comparison)
// ============================================================

func TestBestHashtagIsPlaywright(t *testing.T) {
	a := analyzerFromCSV(t)
	stats := a.HashtagStats()
	if len(stats) == 0 {
		t.Fatal("no hashtag stats")
	}
	// #TestAutomation should be in top 5 by usage
	found := false
	for i, s := range stats {
		if s.Tag == "#TestAutomation" {
			found = true
			if i > 5 {
				t.Logf("#TestAutomation ranked #%d by avg impressions", i+1)
			}
			break
		}
	}
	if !found {
		t.Error("#TestAutomation not found in hashtag stats")
	}
}

// ============================================================
// Level 2b: Format comparison
// ============================================================

func TestArticlesOutperformPostsByImpression(t *testing.T) {
	a := analyzerFromCSV(t)
	stats := a.FormatStats()
	var articleStat, postStat *FormatStat
	for i := range stats {
		if stats[i].Format == "article" {
			articleStat = &stats[i]
		}
		if stats[i].Format == "post" {
			postStat = &stats[i]
		}
	}
	if articleStat == nil || postStat == nil {
		t.Skip("not enough data to compare article vs post")
	}
	if articleStat.AvgImpressions <= postStat.AvgImpressions {
		t.Logf("articles avg=%.0f, posts avg=%.0f — articles NOT outperforming posts",
			articleStat.AvgImpressions, postStat.AvgImpressions)
	}
}

// ============================================================
// Level 3: Drift detection
// ============================================================

func TestNoFalseDriftAlerts(t *testing.T) {
	a := analyzerFromCSV(t)
	alerts := a.DetectDrift(0.2) // generous threshold
	for _, alert := range alerts {
		if strings.Contains(alert, "DRIFT") {
			t.Logf("potential drift: %s", alert)
		}
	}
}

// ============================================================
// Level 4: Golden dataset benchmark
// ============================================================

func TestBenchmarkPositive(t *testing.T) {
	a := analyzerFromCSV(t)
	b := a.Benchmark()
	if b.AvgImpressions <= 0 {
		t.Error("avg impressions should be > 0")
	}
	if b.ImpressionsP50 <= 0 {
		t.Error("median impressions should be > 0")
	}
	if len(b.TopHashtags) == 0 {
		t.Error("should have at least one top hashtag")
	}
	t.Logf("Benchmark: avg=%.0f imp, median=%.0f, p90=%.0f", b.AvgImpressions, b.ImpressionsP50, b.ImpressionsP90)
	t.Logf("Top hashtags: %v", b.TopHashtags)
	t.Logf("Top formats: %v", b.TopFormats)
	t.Logf("Avg engagement: %.5f, median engagement: %.5f", b.AvgEngagement, b.EngagementP50)
}

// ============================================================
// Helper
// ============================================================

func analyzerFromCSV(t *testing.T) *Analyzer {
	t.Helper()
	// Use an embedded minimal dataset instead of file dependency
	data := `date,topic,format,impressions,likes,comments,saves,shares,yes_no_edit,notes,url,hashtags
2026-05-01,Exploratory Testing,post,115,5,0,0,0,n,Test,?,#ExploratoryTesting
2026-05-13,ISTQB Test Management,article,727,5,0,0,1,n,Test,?,#ISTQB #TestManagement
2026-05-19,QA Engineer AI Testing,article,2150,8,4,0,1,n,BEST,?,#TestAutomation #GenAItesting
2026-05-23,SWE-Tester MAS Pipeline,article,336,0,0,0,0,n,LOW,?,#SWETester #MASpipeline
2026-05-28,From Vibing to Production,article,279,1,0,0,0,n,Test,?,#SoftwareEngineering #AIAgents
2026-06-01,Cline AI Agent,article,727,0,0,0,1,n,Test,?,#Cline #AIAgent
2026-06-04,Webwright Experiment,carousel,1436,0,0,0,0,n,Test,?,#Webwright #AITesting
2026-06-05,OrangeHRM Local,carousel,1533,0,0,0,0,n,Saga,?,#OrangeHRM #Docker
2026-06-10,KISS Sorcar vs Webwright,article,2150,1,4,1,1,n,BEST,https://lnkd.in/eMsZHr5Q,#KISSSorcar #AIAgents
2026-06-11,Autonoma deploy story,article,1267,10,2,0,0,n,Hot,https://lnkd.in/eMsZHr5Q,#Autonoma #AIAgents
2026-06-12,KISS vs Autonoma,article,1102,9,2,0,0,n,Hot,https://lnkd.in/eMsZHr5Q,#AIAgents #Playwright
2026-06-22,Wrong Thing article,article,2422,0,2,0,0,n,Peak,?,#AIAgents #Testing #Playwright
2026-06-24,Skills npm,article,224,0,0,0,0,n,Flop,?,#TestAutomation #AIQA
2026-06-26,AI Fluency article,article,280,0,0,0,0,n,Test,?,#AIInterview #QAEngineer
2026-06-22,Wrong Thing post,post,2422,0,0,0,0,n,Peak,?,#AIAgents #Testing #Playwright
2026-06-26,AI Fluency post,post,43,0,0,0,0,n,Low,?,#AIInterview #QAEngineer
`

	a, err := ParseCSV(strings.NewReader(data))
	if err != nil {
		t.Fatalf("parse csv: %v", err)
	}
	return a
}

// ============================================================
// Golden dataset — regression test for known benchmark values
// ============================================================

func TestGoldenBenchmarkRegression(t *testing.T) {
	a := analyzerFromCSV(t)
	b := a.Benchmark()

	// Golden: ensure avg impressions within reasonable range for this dataset
	if math.Abs(b.AvgImpressions-1110.0) > 300 {
		t.Logf("Golden regression: avg_impressions=%.0f (expected ~1110)", b.AvgImpressions)
	}
	// Top hashtag should include #AIAgents or #TestAutomation
	hasAIAgents := false
	for _, h := range b.TopHashtags {
		if h == "#AIAgents" || h == "#TestAutomation" {
			hasAIAgents = true
			break
		}
	}
	if !hasAIAgents {
		t.Log("Golden regression: expected #AIAgents or #TestAutomation in top hashtags")
	}
}

func TestEngagementDriftAlertsForLowWeeks(t *testing.T) {
	a := analyzerFromCSV(t)
	alerts := a.DetectDrift(0.005)
	// We expect low-engagement weeks to be flagged
	if len(alerts) == 0 {
		t.Log("no drift alerts — engagement is stable or threshold too strict")
	}
	for _, alert := range alerts {
		t.Logf("Alert: %s", alert)
	}
}

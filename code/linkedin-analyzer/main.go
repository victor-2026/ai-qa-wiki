package main

import (
	"fmt"
	"os"

	"linkedin-analyzer/analyzer"
)

func main() {
	file := "testdata.csv"
	if len(os.Args) > 1 {
		file = os.Args[1]
	}

	f, err := os.Open(file)
	if err != nil {
		fmt.Fprintf(os.Stderr, "open %s: %v\n", file, err)
		os.Exit(1)
	}
	defer f.Close()

	a, err := analyzer.ParseCSV(f)
	if err != nil {
		fmt.Fprintf(os.Stderr, "parse: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("LinkedIn Performance Analyzer\n")
	fmt.Printf("Posts analyzed: %d\n\n", len(a.Posts))

	// Level 1: Invariants
	v := a.CheckInvariants()
	fmt.Printf("=== Level 1: PBT Invariants ===\n")
	if len(v) == 0 {
		fmt.Printf("  All clean (no violations)\n")
	} else {
		for _, vi := range v {
			fmt.Printf("  VIOLATION: %s\n", vi)
		}
	}

	// Level 2: Hashtags
	fmt.Printf("\n=== Level 2: Hashtag Performance ===\n")
	hs := a.HashtagStats()
	for i, s := range hs {
		if i >= 10 {
			break
		}
		fmt.Printf("  %2d. %-25s avg=%.0f eng=%.4f (used %d times)\n",
			i+1, s.Tag, s.AvgImpressions, s.AvgEngagement, s.Count)
	}

	// Level 2b: Formats
	fmt.Printf("\n=== Format Performance ===\n")
	for _, s := range a.FormatStats() {
		viewsStr := fmt.Sprintf("avg=%.0f views,", s.AvgViews)
		if s.AvgViews == 0 {
			viewsStr = ""
		}
		readStr := fmt.Sprintf("read_rate=%.1f%%", s.AvgReadRate*100)
		if s.AvgReadRate == 0 {
			readStr = "read_rate=N/A"
		}
		fmt.Printf("  %-10s avg=%.0f imp, %s %s, eng=%.4f (%d posts)\n",
			s.Format, s.AvgImpressions, viewsStr, readStr, s.AvgEngagement, s.Count)
	}

	// Level 3: Drift
	fmt.Printf("\n=== Level 3: Weekly Drift ===\n")
	alerts := a.DetectDrift(0.01)
	if len(alerts) == 0 {
		fmt.Printf("  No significant drift detected\n")
	} else {
		for _, al := range alerts {
			fmt.Printf("  DRIFT: %s\n", al)
		}
	}

	// Level 4: Benchmark
	fmt.Printf("\n=== Level 4: Golden Benchmark ===\n")
	b := a.Benchmark()
	fmt.Printf("  Avg impressions:  %.0f\n", b.AvgImpressions)
	fmt.Printf("  Median (P50):     %.0f\n", b.ImpressionsP50)
	fmt.Printf("  P90:              %.0f\n", b.ImpressionsP90)
	fmt.Printf("  Avg engagement:   %.5f\n", b.AvgEngagement)
	fmt.Printf("  Top hashtags:     %v\n", b.TopHashtags)
	fmt.Printf("  Top formats:      %v\n", b.TopFormats)
}

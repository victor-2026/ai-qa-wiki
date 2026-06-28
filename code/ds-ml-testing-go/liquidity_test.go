package liquidity

import (
	"math"
	"testing"
)

// ============================================================
// Level 1: Property-Based Tests (PBT) — инварианты модели
// ============================================================

// Invariant 1: All shares sum to 1.0 (± rounding)
func TestAllocationSharesSumToOne(t *testing.T) {
	a := NewAllocator(1000.0)
	ads := []Ad{
		{ID: "a1", Rating: 5.0, Budget: 200, History: 0.8, Priority: 1},
		{ID: "a2", Rating: 3.0, Budget: 100, History: 0.5, Priority: 2},
		{ID: "a3", Rating: 1.0, Budget: 50, History: 0.1, Priority: 3},
	}
	result := a.Allocate(ads)
	var totalShare float64
	for _, r := range result {
		totalShare += r.Share
	}
	// допускаем погрешность округления 0.001
	if math.Abs(totalShare-1.0) > 0.001 {
		t.Errorf("shares sum to %.4f, want ~1.0", totalShare)
	}
}

// Invariant 2: No negative shares
func TestAllocationSharesNonNegative(t *testing.T) {
	a := NewAllocator(500.0)
	ads := []Ad{
		{ID: "a1", Rating: -1.0, Budget: 0, History: 0, Priority: 1},
		{ID: "a2", Rating: 0, Budget: 0, History: 0, Priority: 1},
	}
	result := a.Allocate(ads)
	for _, r := range result {
		if r.Share < 0 {
			t.Errorf("negative share for ad %s: %.4f", r.AdID, r.Share)
		}
	}
}

// Invariant 3: Total allocated amount = TotalLiquidity (± rounding)
func TestAllocationTotalAmount(t *testing.T) {
	total := 1234.56
	a := NewAllocator(total)
	ads := []Ad{
		{ID: "a1", Rating: 4.5, Budget: 300, History: 0.9, Priority: 1},
		{ID: "a2", Rating: 3.8, Budget: 200, History: 0.6, Priority: 1},
		{ID: "a3", Rating: 2.0, Budget: 100, History: 0.3, Priority: 2},
	}
	result := a.Allocate(ads)
	var totalAmount float64
	for _, r := range result {
		totalAmount += r.Amount
	}
	if math.Abs(totalAmount-total) > 0.01 {
		t.Errorf("allocated $%.2f, want $%.2f", totalAmount, total)
	}
}

// Invariant 4: Higher rating → higher share (при равных прочих)
func TestHigherRatingGetsMore(t *testing.T) {
	a := NewAllocator(1000.0)
	ads := []Ad{
		{ID: "low", Rating: 1.0, Budget: 100, History: 0.5, Priority: 1},
		{ID: "high", Rating: 5.0, Budget: 100, History: 0.5, Priority: 1},
	}
	result := a.Allocate(ads)
	var lowShare, highShare float64
	for _, r := range result {
		if r.AdID == "low" {
			lowShare = r.Share
		}
		if r.AdID == "high" {
			highShare = r.Share
		}
	}
	if highShare <= lowShare {
		t.Errorf("high-rating ad share %.4f <= low-rating ad share %.4f", highShare, lowShare)
	}
}

// ============================================================
// Level 1b: Table-driven PBT (edge cases)
// ============================================================

func TestAllocationEdgeCases(t *testing.T) {
	tests := []struct {
		name  string
		total float64
		ads   []Ad
		want  int // expected number of allocations
	}{
		{"single ad", 100.0, []Ad{{ID: "a1", Rating: 3.0, Budget: 100, History: 0.5, Priority: 1}}, 1},
		{"no ads", 100.0, []Ad{}, 0},
		{"zero rating", 100.0, []Ad{{ID: "a1", Rating: 0, Budget: 100, History: 0, Priority: 1}}, 1},
		{"zero liquidity", 0.0, []Ad{{ID: "a1", Rating: 5.0, Budget: 100, History: 0.9, Priority: 1}}, 1},
		{"all same params", 500.0, []Ad{
			{ID: "a1", Rating: 3.0, Budget: 100, History: 0.5, Priority: 1},
			{ID: "a2", Rating: 3.0, Budget: 100, History: 0.5, Priority: 1},
		}, 2},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			a := NewAllocator(tt.total)
			got := a.Allocate(tt.ads)
			if len(got) != tt.want {
				t.Errorf("got %d allocations, want %d", len(got), tt.want)
			}
			// invariant check for every case
			var sum float64
			for _, r := range got {
				sum += r.Share
			}
			if len(got) > 0 && math.Abs(sum-1.0) > 0.001 {
				t.Errorf("shares sum to %.4f, want ~1.0", sum)
			}
		})
	}
}

// ============================================================
// Level 2: A/B Experiment Gate (mock)
// ============================================================

// SimulateModel is a mock model for A/B comparison
type SimulateModel struct {
	Name string
	Bias float64 // systematic bias vs current model
	Noise float64 // random noise stddev
}

func SimulateABTest(current, experiment SimulateModel, n int) (better bool, pValue float64) {
	var currentWins, experimentWins int
	for i := 0; i < n; i++ {
		// simple simulation: higher score = better allocation
		cScore := 50.0 + current.Bias + current.Noise*float64(i%10-5)/5
		eScore := 50.0 + experiment.Bias + experiment.Noise*float64(i*7%10-5)/5
		if eScore > cScore {
			experimentWins++
		} else {
			currentWins++
		}
	}
	// mock significance: experiment needs >55% wins
	ratio := float64(experimentWins) / float64(n)
	better = ratio > 0.55
	// mock p-value (chi-squared approximation)
	pValue = 1.0 - (ratio-0.5)*2
	if pValue < 0 {
		pValue = 0
	}
	return better, pValue
}

func TestABGate_PassesWithGoodModel(t *testing.T) {
	current := SimulateModel{Name: "v1", Bias: 0, Noise: 5}
	experiment := SimulateModel{Name: "v2_better", Bias: 3, Noise: 5}
	better, _ := SimulateABTest(current, experiment, 1000)
	if !better {
		t.Error("better model should pass A/B gate")
	}
}

func TestABGate_RejectsWorseModel(t *testing.T) {
	current := SimulateModel{Name: "v1", Bias: 0, Noise: 3}
	experiment := SimulateModel{Name: "v2_worse", Bias: -2, Noise: 3}
	better, _ := SimulateABTest(current, experiment, 500)
	if better {
		t.Error("worse model should NOT pass A/B gate")
	}
}

// ============================================================
// Level 3: Drift Detection (mock)
// ============================================================

type DistributionStats struct {
	Mean   float64
	StdDev float64
	Min    float64
	Max    float64
}

func ComputeStats(values []float64) DistributionStats {
	if len(values) == 0 {
		return DistributionStats{}
	}
	var sum, sumSq float64
	min, max := values[0], values[0]
	for _, v := range values {
		sum += v
		sumSq += v * v
		if v < min {
			min = v
		}
		if v > max {
			max = v
		}
	}
	n := float64(len(values))
	mean := sum / n
	variance := sumSq/n - mean*mean
	if variance < 0 {
		variance = 0
	}
	return DistributionStats{
		Mean:   mean,
		StdDev: math.Sqrt(variance),
		Min:    min,
		Max:    max,
	}
}

// DetectDrift compares two distributions using PSI (Population Stability Index).
// PSI > 0.1 indicates significant drift.
func DetectDrift(baseline, current []float64) (psi float64, drifted bool) {
	if len(baseline) == 0 || len(current) == 0 {
		return 0, false
	}
	bStats := ComputeStats(baseline)
	cStats := ComputeStats(current)

	// simplified PSI: compare means normalized by stddev
	meanDiff := math.Abs(cStats.Mean - bStats.Mean)
	if bStats.StdDev > 0 {
		psi = meanDiff / bStats.StdDev
	}
	return psi, psi > 0.1
}

func TestDriftDetection_SameDistribution(t *testing.T) {
	baseline := []float64{100, 102, 98, 101, 99, 103, 97, 100, 102, 98}
	current := []float64{99, 101, 100, 102, 98, 100, 101, 99, 100, 101}
	psi, drifted := DetectDrift(baseline, current)
	if drifted {
		t.Errorf("same distribution flagged as drift: PSI=%.4f", psi)
	}
}

func TestDriftDetection_ShiftedDistribution(t *testing.T) {
	baseline := []float64{100, 102, 98, 101, 99, 103, 97, 100, 102, 98}
	current := []float64{150, 152, 148, 151, 149, 153, 147, 150, 152, 148}
	psi, drifted := DetectDrift(baseline, current)
	if !drifted {
		t.Errorf("shifted distribution NOT flagged: PSI=%.4f", psi)
	}
}

// ============================================================
// Level 4: Golden Dataset Regression
// ============================================================

type GoldenRecord struct {
	Ads      []Ad
	Total    float64
	Expected []Allocation
}

func (g GoldenRecord) Equal(result []Allocation) bool {
	if len(result) != len(g.Expected) {
		return false
	}
	for i := range result {
		if result[i].AdID != g.Expected[i].AdID {
			return false
		}
		if math.Abs(result[i].Share-g.Expected[i].Share) > 0.0001 {
			return false
		}
	}
	return true
}

func TestGoldenDataset_Regression(t *testing.T) {
	golden := GoldenRecord{
		Total: 1000.0,
		Ads: []Ad{
			{ID: "a1", Rating: 5.0, Budget: 200, History: 0.8, Priority: 1},
			{ID: "a2", Rating: 3.0, Budget: 100, History: 0.5, Priority: 2},
			{ID: "a3", Rating: 1.0, Budget: 50, History: 0.1, Priority: 3},
		},
		Expected: []Allocation{
			{AdID: "a1", Share: 0.7747, Amount: 774.70},
			{AdID: "a2", Share: 0.1937, Amount: 193.70},
			{AdID: "a3", Share: 0.0316, Amount: 31.60},
		},
	}

	a := NewAllocator(golden.Total)
	result := a.Allocate(golden.Ads)

	if !golden.Equal(result) {
		t.Error("golden dataset regression FAILED — model output changed")
		for i, r := range result {
			if i < len(golden.Expected) {
				t.Logf("  ad %s: got share=%.4f want share=%.4f", r.AdID, r.Share, golden.Expected[i].Share)
			}
		}
	}
}

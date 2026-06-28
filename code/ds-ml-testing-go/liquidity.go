package liquidity

import "math"

type Ad struct {
	ID       string
	Rating   float64 // 0.0–5.0
	Budget   float64 // remaining budget, $
	History  float64 // historical conversion, 0.0–1.0
	Priority int     // 1=high, 2=medium, 3=low
}

type Allocation struct {
	AdID   string
	Share  float64 // allocated liquidity share, 0.0–1.0
	Amount float64 // allocated amount in $
}

type Allocator struct {
	TotalLiquidity float64
}

func NewAllocator(total float64) *Allocator {
	return &Allocator{TotalLiquidity: total}
}

// Allocate distributes total liquidity among ads.
// Algorithm: weighted by Rating * (1+History) / Priority
func (a *Allocator) Allocate(ads []Ad) []Allocation {
	if len(ads) == 0 {
		return nil
	}

	weights := make([]float64, len(ads))
	var totalWeight float64

	for i, ad := range ads {
		score := ad.Rating * (1 + ad.History) / float64(ad.Priority)
		if score < 0 {
			score = 0
		}
		weights[i] = score
		totalWeight += score
	}

	result := make([]Allocation, len(ads))
	if totalWeight <= 0 {
		equalShare := roundTo(1.0/float64(len(ads)), 4)
		for i, ad := range ads {
			result[i] = Allocation{
				AdID:   ad.ID,
				Share:  equalShare,
				Amount: roundTo(equalShare*a.TotalLiquidity, 2),
			}
		}
		return result
	}
	for i, ad := range ads {
		share := weights[i] / totalWeight
		result[i] = Allocation{
			AdID:   ad.ID,
			Share:  roundTo(share, 4),
			Amount: roundTo(share*a.TotalLiquidity, 2),
		}
	}
	return result
}

func roundTo(v float64, decimals int) float64 {
	pow := math.Pow(10, float64(decimals))
	return math.Round(v*pow) / pow
}

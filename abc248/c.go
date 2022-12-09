package main

import (
	"fmt"
	"math"
)

func main() {
	var n, m, k int
	fmt.Scan(&n, &m, &k)
	var dp [51][51 * 51]uint64
	//var dp [3][3 * 5]uint64
	var sum uint64
	for i := 0; i < n+1; i++ {
		for j := 0; j < k+1; j++ {
			dp[i][j] = 0
		}
	}
	for j := 1; j < m+1; j++ {
		dp[1][j] = 1
	}
	//fmt.Println(dp)
	for i := 1; i < n; i++ {
		for j := 1; j < k+1; j++ {
			//fmt.Println(j, int(math.Min(float64(m), float64(j-1)))+1)
			for l := 1; l < int(math.Min(float64(m), float64(j-1)))+1; l++ {
				dp[i+1][j] += dp[i][j-l]
				dp[i+1][j] %= 998244353
			}
		}
		//fmt.Println(dp)

	}
	//fmt.Println(dp)
	sum = 0
	for j := 0; j < k+1; j++ {
		sum += dp[n][j]
		sum %= 998244353
	}
	fmt.Println(sum)
}

package main

import (
	"fmt"
)

func main() {
	var n int
	var paths = [9]uint64{1, 1, 1, 1, 1, 1, 1, 1, 1}
	var prev [9]uint64
	fmt.Scan(&n)

	for i := 1; i < n; i++ {
		prev = paths
		for j := 0; j < 9; j++ {
			if j == 0 {
				paths[j] = (prev[j] + prev[j+1]) % 998244353
			} else if j == 8 {
				paths[j] = (prev[j-1] + prev[j]) % 998244353
			} else {
				paths[j] = (prev[j-1] + prev[j] + prev[j+1]) % 998244353
			}
		}
	}
	//fmt.Println(paths)
	var sum uint64
	sum = 0

	for _, x := range paths {
		sum += x
	}
	fmt.Println(sum % 998244353)
}

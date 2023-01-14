package main

import (
	"fmt"
	"sort"
)

func ReverseInts(ints []int) {
	// https://stackoverflow.com/a/10030772
	for i, j := 0, len(ints)-1; i < j; i, j = i+1, j-1 {
		ints[i], ints[j] = ints[j], ints[i]
	}
}

func Sum(ints []int) int {
	result := 0
	for _, v := range ints {
		result += v
	}
	return result
}

func InputIntArray(n int) []int {
	result := make([]int, n)
	for i := range result {
		fmt.Scanf("%d", &result[i])
	}
	return result
}

func main() {
	var N, K int
	fmt.Scanf("%d %d", &N, &K)
	H := InputIntArray(N)

	sort.Ints(H)
	ReverseInts(H)

	var ans int
	if N <= K {
		ans = 0
	} else {
		ans = Sum(H[K:])
	}

	fmt.Println(ans)
}

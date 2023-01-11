package main

import (
	"fmt"
)

func InputIntArray(n int) []int {
	result := make([]int, n)
	for i := range result {
		fmt.Scanf("%d", &result[i])
	}
	return result
}

func Solve(x int, hs []int) int {
	if len(hs) == 0 {
		return 0
	}

	h := hs[0]
	hs = hs[1:]

	if x <= h {
		return Solve(h, hs) + 1
	} else {
		return Solve(x, hs)
	}
}

func main() {
	var N int
	fmt.Scanf("%d", &N)
	H := InputIntArray(N)

	ans := Solve(0, H)

	fmt.Println(ans)
}

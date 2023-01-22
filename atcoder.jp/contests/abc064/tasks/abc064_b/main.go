package main

import (
	"fmt"
)

func InputInt() int {
	var n int
	fmt.Scanf("%d", &n)
	return n
}

func InputIntArray(n int) []int {
	result := make([]int, n)
	for i := range result {
		fmt.Scanf("%d", &result[i])
	}
	return result
}

func main() {
	N := InputInt()
	A := InputIntArray(N)

	max := 0
	min := 10000

	for _, v := range A {
		if max < v {
			max = v
		}
		if v < min {
			min = v
		}
	}

	ans := max - min

	fmt.Println(ans)
}

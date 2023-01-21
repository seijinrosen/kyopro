package main

import (
	"fmt"
	"strconv"
	"strings"
)

func PrintIntArray(arr []int) {
	var result []string
	for _, v := range arr {
		result = append(result, strconv.Itoa(v))
	}
	fmt.Println(strings.Join(result, " "))
}

func InputIntArray(n int) []int {
	result := make([]int, n)
	for i := range result {
		fmt.Scanf("%d", &result[i])
	}
	return result
}

func main() {
	var N, P, Q, R, S int
	fmt.Scanf("%d %d %d %d %d", &N, &P, &Q, &R, &S)

	A := InputIntArray(N)

	var ans []int
	ans = append(ans, A[:P-1]...)
	ans = append(ans, A[R-1:S]...)
	ans = append(ans, A[Q:R-1]...)
	ans = append(ans, A[P-1:Q]...)
	ans = append(ans, A[S:]...)

	PrintIntArray(ans)
}

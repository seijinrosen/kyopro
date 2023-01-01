package main

import (
	"fmt"
)

func Solve(n int) int {
	if n <= 125 {
		return 4
	}
	if n <= 211 {
		return 6
	}
	return 8
}

func main() {
	var N int
	fmt.Scanf("%d", &N)

	ans := Solve(N)

	fmt.Println(ans)
}

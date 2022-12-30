package main

import (
	"fmt"
	"math"
)

func Compare(x, y float64) string {
	if x < y {
		return "<"
	}
	if x > y {
		return ">"
	}
	return "="
}

func Solve(a, b float64, c int) string {
	if c%2 == 0 {
		return Compare(math.Abs(a), math.Abs(b))
	} else {
		return Compare(a, b)
	}
}

func main() {
	var A, B float64
	var C int
	fmt.Scanf("%g %g %d", &A, &B, &C)

	ans := Solve(A, B, C)

	fmt.Println(ans)
}

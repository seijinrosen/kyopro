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

func main() {
	var A, B float64
	fmt.Scanf("%g %g", &A, &B)

	var ans string
	switch Compare(math.Abs(A), math.Abs(B)) {
	case "<":
		ans = "Ant"
	case "=":
		ans = "Draw"
	case ">":
		ans = "Bug"
	}

	fmt.Println(ans)
}

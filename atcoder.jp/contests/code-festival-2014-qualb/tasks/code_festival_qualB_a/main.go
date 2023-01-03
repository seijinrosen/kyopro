package main

import (
	"fmt"
	"math"
)

func main() {
	var A, B float64
	fmt.Scanf("%g %g", &A, &B)

	ans := math.Max(A, B)

	fmt.Println(ans)
}

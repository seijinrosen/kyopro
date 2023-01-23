package main

import (
	"fmt"
	"math"
)

func main() {
	var a float64
	fmt.Scanf("%g", &a)

	ans := a + math.Pow(a, 2) + math.Pow(a, 3)

	fmt.Println(ans)
}

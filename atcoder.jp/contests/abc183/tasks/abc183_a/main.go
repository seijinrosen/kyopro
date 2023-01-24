package main

import (
	"fmt"
)

func relu(x int) int {
	if x >= 0 {
		return x
	}
	return 0
}

func main() {
	var x int
	fmt.Scanf("%d", &x)

	ans := relu(x)

	fmt.Println(ans)
}

package main

import (
	"fmt"
)

func main() {
	var X, Y, Z int
	fmt.Scanf("%d %d %d", &X, &Y, &Z)

	ans := (X - Z) / (Y + Z)

	fmt.Println(ans)
}

package main

import (
	"fmt"
	"os"
)

func main() {
	var a, b, c, K int
	fmt.Scanf("%d %d %d", &a, &b, &c)
	fmt.Scanf("%d", &K)

	for i := 0; i <= K; i++ {
		if a < b && b < c {
			fmt.Println("Yes")
			os.Exit(0)
		}

		if a >= b {
			b *= 2
		} else if b >= c {
			c *= 2
		}
	}

	fmt.Println("No")
}

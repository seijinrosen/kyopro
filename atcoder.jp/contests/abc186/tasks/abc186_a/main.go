package main

import (
	"fmt"
)

func main() {
	var N, W int
	fmt.Scanf("%d %d", &N, &W)

	ans := N / W

	fmt.Println(ans)
}

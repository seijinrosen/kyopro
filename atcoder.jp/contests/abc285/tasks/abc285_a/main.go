package main

import (
	"fmt"
)

func YesNo(b bool) string {
	if b {
		return "Yes"
	} else {
		return "No"
	}
}

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	ans := a == b/2

	fmt.Println(YesNo(ans))
}

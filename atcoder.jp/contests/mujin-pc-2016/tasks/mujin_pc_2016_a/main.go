package main

import (
	"fmt"
	"strings"
)

func YesNo(b bool) string {
	if b {
		return "Right"
	} else {
		return "Left"
	}
}

func main() {
	var c string
	fmt.Scanf("%s", &c)

	ans := strings.Contains("OPKL", c)

	fmt.Println(YesNo(ans))
}

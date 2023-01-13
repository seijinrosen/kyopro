package main

import (
	"fmt"
	"strings"
)

func YesNo(b bool) string {
	if b {
		return "Yes"
	} else {
		return "No"
	}
}

func main() {
	var S string
	fmt.Scanf("%s", &S)

	ans := strings.HasPrefix(S, "YAKI")

	fmt.Println(YesNo(ans))
}

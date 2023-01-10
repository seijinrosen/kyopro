package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scanf("%s", &s)

	ans := s[:4] + " " + s[4:]

	fmt.Println(ans)
}

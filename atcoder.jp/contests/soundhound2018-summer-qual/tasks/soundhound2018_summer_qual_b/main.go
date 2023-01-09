package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scanf("%s", &S)
	var w int
	fmt.Scanf("%d", &w)

	var ans []byte
	for i := 0; i < len(S); i += w {
		ans = append(ans, S[i])
	}

	fmt.Println(string(ans))
}

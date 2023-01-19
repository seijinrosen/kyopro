package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scanf("%s", &S)

	T := "CODEFESTIVAL2016"

	ans := 0
	for i := 0; i < 16; i++ {
		if S[i] != T[i] {
			ans++
		}
	}

	fmt.Println(ans)
}

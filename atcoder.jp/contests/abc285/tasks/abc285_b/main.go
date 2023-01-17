package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)
	var S string
	fmt.Scanf("%s", &S)

	for i := 1; i < N; i++ {
		l := 0

		for k := 0; k < N-i; k++ {
			if S[k] == S[k+i] {
				break
			}
			l++
		}

		fmt.Println(l)
	}
}

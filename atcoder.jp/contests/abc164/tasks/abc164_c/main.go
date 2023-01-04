package main

import (
	"fmt"
)

func main() {
	var N int
	fmt.Scanf("%d", &N)

	S := make([]string, N)
	for i := range S {
		fmt.Scanf("%s", &S[i])
	}

	set := make(map[string]struct{})
	for _, v := range S {
		set[v] = struct{}{}
	}

	ans := len(set)

	fmt.Println(ans)
}

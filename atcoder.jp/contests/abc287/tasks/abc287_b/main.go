package main

import (
	"fmt"
)

func InputStringArrayVertically(n int) []string {
	result := make([]string, n)
	for i := range result {
		fmt.Scanf("%s", &result[i])
	}
	return result
}

func main() {
	var N, M int
	fmt.Scanf("%d %d", &N, &M)
	S := InputStringArrayVertically(N)
	T := InputStringArrayVertically(M)

	ans := 0
	for _, s := range S {
		for _, t := range T {
			if s[3:] == t {
				ans++
				break
			}
		}
	}

	fmt.Println(ans)
}

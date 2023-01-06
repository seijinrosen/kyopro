package main

import (
	"fmt"
)

func Dedup(s string) string {
	if len(s) <= 1 {
		return s
	}
	var result []byte
	result = append(result, s[0])
	for i := 1; i < len(s); i++ {
		if s[i-1] != s[i] {
			result = append(result, s[i])
		}
	}
	return string(result)
}

func main() {
	var N int
	fmt.Scanf("%d", &N)
	var S string
	fmt.Scanf("%s", &S)

	ans := len(Dedup(S))

	fmt.Println(ans)
}

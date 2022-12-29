package main

import (
	"fmt"
	"strings"
)

func IsPalindrome(s string) bool {
	return Reverse(s) == s
}

func Reverse(s string) string {
	// https://stackoverflow.com/a/10030772
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func YesNo(b bool) string {
	if b {
		return "Yes"
	} else {
		return "No"
	}
}

func main() {
	var N string
	fmt.Scanf("%s", &N)

	ans := IsPalindrome(strings.TrimRight(N, "0"))

	fmt.Println(YesNo(ans))
}

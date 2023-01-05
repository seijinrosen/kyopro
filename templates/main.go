package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func Compare(x, y float64) string {
	if x < y {
		return "<"
	}
	if x > y {
		return ">"
	}
	return "="
}

func IsPalindrome(s string) bool {
	return Reverse(s) == s
}

func IsWeak2(xs []int) bool {
	// https://atcoder.jp/contests/abc212/tasks/abc212_b
	if len(xs) < 2 {
		return true
	}
	x := xs[0]
	y := xs[1]
	xs = xs[1:]
	return (x+1)%10 == y && IsWeak2(xs)
}

func Reverse(s string) string {
	// https://stackoverflow.com/a/10030772
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func StringToDigits(s string) []int {
	digits := make([]int, len(s))
	for i, c := range strings.Split(s, "") {
		digits[i], _ = strconv.Atoi(c)
	}
	return digits
}

func YesNo(b bool) string {
	if b {
		return "Yes"
	} else {
		return "No"
	}
}

func Solve(a, b float64, c int) string {
	if c%2 == 0 {
		return Compare(math.Abs(a), math.Abs(b))
	} else {
		return Compare(a, b)
	}
}

func main() {
	var N int
	fmt.Scanf("%d", &N)

	var S string
	fmt.Scanf("%s", &S)

	var A, B float64
	var C int
	fmt.Scanf("%g %g %d", &A, &B, &C)

	// S := make([]string, N)
	// for i := range S {
	// 	fmt.Scanf("%s", &S[i])
	// }

	ans := IsPalindrome(strings.TrimRight(S, "0"))

	// set := make(map[string]struct{})
	// for _, v := range S {
	// 	set[v] = struct{}{}
	// }
	// ans := len(set)

	fmt.Println(ans)
	fmt.Println(YesNo(ans))
}

package main

import (
	"fmt"
	"strconv"
	"strings"
)

func StringToDigits(s string) []int {
	digits := make([]int, len(s))
	for i, c := range strings.Split(s, "") {
		digits[i], _ = strconv.Atoi(c)
	}
	return digits
}

func YesNo(b bool) string {
	if b {
		return "Weak"
	} else {
		return "Strong"
	}
}

func IsWeak1(xs []int) bool {
	set := make(map[int]struct{})
	for _, v := range xs {
		set[v] = struct{}{}
	}
	return len(set) == 1
}

func IsWeak2(xs []int) bool {
	if len(xs) < 2 {
		return true
	}
	x := xs[0]
	y := xs[1]
	xs = xs[1:]
	return (x+1)%10 == y && IsWeak2(xs)
}

func main() {
	var XS string
	fmt.Scanf("%s", &XS)

	digits := StringToDigits(XS)

	fmt.Println(YesNo(IsWeak1(digits) || IsWeak2(digits)))
}

package main

import (
	"fmt"
)

func YesNo(b bool) string {
	if b {
		return "Yes"
	} else {
		return "No"
	}
}

func InputInt() int {
	var n int
	fmt.Scanf("%d", &n)
	return n
}

func InputStringArrayVertically(n int) []string {
	result := make([]string, n)
	for i := range result {
		fmt.Scanf("%s", &result[i])
	}
	return result
}

func main() {
	N := InputInt()
	S := InputStringArrayVertically(N)

	cnt := 0
	for _, v := range S {
		if v == "For" {
			cnt++
		}
	}

	ans := N/2 < cnt

	fmt.Println(YesNo(ans))
}

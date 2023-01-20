package main

import (
	"fmt"
)

func YesNo(b bool) string {
	if b {
		return "YES"
	} else {
		return "NO"
	}
}

func InputInt() int {
	var n int
	fmt.Scanf("%d", &n)
	return n
}

func InputIntArray(n int) []int {
	result := make([]int, n)
	for i := range result {
		fmt.Scanf("%d", &result[i])
	}
	return result
}

func main() {
	N := InputInt()
	P := InputIntArray(N)

	cnt := 0
	for i, p := range P {
		if i+1 != p {
			cnt++
		}
	}

	ans := cnt == 0 || cnt == 2

	fmt.Println(YesNo(ans))
}

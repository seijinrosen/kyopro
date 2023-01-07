package main

import (
	"fmt"
)

func ReverseStringArray(array []string) []string {
	result := make([]string, len(array))
	for i, s := range array {
		result[len(array)-1-i] = s
	}
	return result
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

	for _, s := range ReverseStringArray(S) {
		fmt.Println(s)
	}
}

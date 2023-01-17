package main

import (
	"fmt"
)

func main() {
	var N, K int
	fmt.Scanf("%d %d", &N, &K)

	set := make(map[int]struct{})

	for i := 0; i < K; i++ {
		var d int
		fmt.Scanf("%d", &d)

		for i := 0; i < d; i++ {
			var a int
			fmt.Scanf("%d", &a)

			set[a] = struct{}{}
		}
	}

	ans := N - len(set)

	fmt.Println(ans)
}

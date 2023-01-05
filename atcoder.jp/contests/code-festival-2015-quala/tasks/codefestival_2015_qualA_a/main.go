package main

import (
	"fmt"
)

func main() {
	var S string
	fmt.Scanf("%s", &S)

	ans := S[:len(S)-1] + "5"

	fmt.Println(ans)
}

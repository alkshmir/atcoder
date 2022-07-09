package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	r := bufio.NewReader(os.Stdin)
	w := bufio.NewWriter(os.Stdout)
	defer w.Flush()

	var N, Q int
	var S string
	fmt.Scan(&N, &Q)
	fmt.Scan(&S)
	t := make([]int, Q)
	x := make([]int, Q)
	for i := 0; i < Q; i++ {
		//fmt.Scan(&t[i], &x[i])
		fmt.Fscan(r, &t[i], &x[i])
	}

	p := 0
	for i := 0; i < Q; i++ {
		if t[i] == 1 {
			//S = S[N-x[i]:] + S[0:N-x[i]]
			p += x[i]
		} else if t[i] == 2 {
			//fmt.Println(string(S[x[i]-1]))
			//fmt.Println(string(S[((x[i]-p-1)%N+N)%N]))
			fmt.Fprintln(w, string(S[((x[i]-p-1)%N+N)%N]))
		}

	}
}

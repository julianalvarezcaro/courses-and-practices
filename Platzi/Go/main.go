package main

import (
	"fmt"
)

var a int
type dinero int
var b dinero

func main () {
	b = dinero(a)
	fmt.Println(a)
}

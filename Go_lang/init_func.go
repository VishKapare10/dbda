package main

import "fmt"

//Variable initialization
var name string
var no int

//init function
func init() {
    fmt.Println("Inside init function")
    name = "Vishwambhar"
    no = 34
}

//main functionB
func main() {
    fmt.Println("Inside main function")
    fmt.Printf("Name: %s, No: %d\n", name,no)
}

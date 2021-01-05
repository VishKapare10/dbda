package main

import "fmt"


func main(){

  var a [2]string
  a[0] = "Vishwambhar"
  a[1] = "Kapare"
  fmt.Println(a)

  num := [5]int{11,34,55,67,99}

  //for loop to iterate array elements
  for i := 0; i< len(num) ; i++ {
    fmt.Println(num[i])
    }
  //fmt.Println(num)
}

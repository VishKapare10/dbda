package main

// import the 2 modules we need
import (
    "fmt"
)

func add(a int, b int) int{
  return a + b
}


func main()  {
  //for loop
  for i:= 0; i<8 ;i ++ {
    fmt.Println("sum is:", add(20,100))
  }

}

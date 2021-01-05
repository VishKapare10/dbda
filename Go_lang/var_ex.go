package main

import "fmt"

func main() {
   var x float64 = 20.0 //static Variable declaration

   y := "abc" //dynamic varible declaration
   fmt.Println(x)
   fmt.Println(y)
   fmt.Printf("x is of type %T\n", x)
   fmt.Printf("y is of type %T\n", y)

   if x ==20.0{
     fmt.Println(x)
   }
   for true  {
       fmt.Printf("This loop will run forever.\n");
     }

}

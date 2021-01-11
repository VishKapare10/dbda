package main

/*
extern void display();
extern int add(int, int);
*/
import "C"
import "fmt"

func main() {
    C.display()
    result := C.add(20,50)
    fmt.Println("Addition =", result)
}

package main
/*
extern void display_msg();
extern int add_integers(int, int);
extern int start(int, int);
*/
import "C"
import "fmt"


func main() {
    C.display_msg()
    result := C.add_integers(100,50)
    fmt.Println("Addition =", result)
    C.start(100,50);
}

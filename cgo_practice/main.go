package main

/*
#include <stdlib.h>
#include "callback.h"
void pmdb_read(void*);
void pmdb_apply(void*);
void pmdb_exec(void*);
*/
import "C"
import (
        "fmt"
        "strings"
        "unsafe"
        //"reflect"
        "github.com/mattn/go-pointer"
        guuid "github.com/google/uuid"
)

type Funcp struct {
        v int
}

type String_data struct {
    data_str string
    to_find string
}


func main() {
        f := &Funcp{10}

        raft_uuid := guuid.New()
        //fmt.Printf("raft uuid: %s\n", raft_uuid.String())
        raft_uuid_str := C.CString(raft_uuid.String())

        my_uuid := guuid.New()
        //fmt.Printf("my uuid: %s\n", my_uuid.String())
        my_uuid_str := C.CString(my_uuid.String())

        //fmt.Println("Type of var my_uuid_str = ", reflect.TypeOf(my_uuid.String()))
        C.call_pmdb_exec(C.callback(C.pmdb_exec), pointer.Save(f), raft_uuid_str, my_uuid_str)

        s := &String_data{"India has been the one major deviant case for consociational (power-sharing) theory, and its sheer size makes the exception especially damaging. A deeply divided society with, supposedly, a mainly majoritarian type of democracy, India nevertheless has been able to maintain its democratic system. Careful examination reveals, however, that Indian democracy has displayed all four crucial elements of power-sharing theory. In fact, it was a perfectly and thoroughly consociational system during its first two decades. From the late 1960s on, although India has remained basically consociational, some of its power-sharing elements have weakened under the pressure of greater mass mobilization. Concomitantly, in accordance with consociational theory, intergroup hostility and violence have increased. Therefore, India is not a deviant case for consociational theory but, instead, an impressive confirming case.", ""}
        s.to_find = "consociational"


        C.call_pmdb_read(C.callback(C.pmdb_read), pointer.Save(s))
}

//export pmdb_read
func pmdb_read(data unsafe.Pointer){
        fmt.Println("In pmdb read")
        f := pointer.Restore(data).(*String_data)
        fmt.Println("Data :",f.data_str)
        fmt.Println("To find:", f.to_find)

        //calling apply function to get map of (word:counts)
        mp := apply(f.data_str)

        //printing map of (word:counts)
        for i,j := range mp{
                fmt.Println(i,"==>",j)
                }

        //calling function get_count_of_word to get count of given word
        cnt := get_count_of_word(mp, f.to_find)

        //printing count of given word
        for i,j := range cnt{
                fmt.Println("Count of word",i,"=>",j)
                }
}


func apply(str string) map[string]int {

    c := strings.Split(str, ",")
    justString := strings.Join(c," ")
    res := strings.Replace(justString, ".", " ",-1)

    words := strings.Split(res, " ")

    wordCountMap := make(map[string]int)

    for _,word := range words{
        wordCountMap[word]++
    }

    return wordCountMap
}


func get_count_of_word(counts map[string]int, s string) map[string]int {
   count_of_word := make(map[string]int)
   if value, ok := counts[s]; ok {
                fmt.Println("Key found")
                count_of_word[s] = value
                } else {
                fmt.Println("key not found")
        }
   return count_of_word
}

//export pmdb_exec
func pmdb_exec(data unsafe.Pointer) {

        fmt.Println("In pmdb exec")

}

package main

import "C"
import (
        "fmt"
        "strings"
        "unsafe"
        "github.com/mattn/go-pointer"
        guuid "github.com/google/uuid"
)


type String_data struct {
    data_str string
}

type UUID struct {
    raft_uuid string
    my_uuid string
}

type MapS struct {
    my_map map[string]int
}

func main() {
        fmt.Println("In main function")
        raft_uuid := guuid.New()
        fmt.Printf("Generated raft uuid: %s\n", raft_uuid.String())

        my_uuid := guuid.New()
        fmt.Printf("Generated my uuid: %s\n", my_uuid.String())

        uuid_data := &UUID{raft_uuid.String(), my_uuid.String()}
        fmt.Println(uuid_data)

        s := &String_data{"India has been the one major deviant case for consociational (power-sharing) theory, and its sheer size makes the exception especially damaging. A deeply divided society with, supposedly, a mainly majoritarian type of democracy, India nevertheless has been able to maintain its democratic system. Careful examination reveals, however, that Indian democracy has displayed all four crucial elements of power-sharing theory. In fact, it was a perfectly and thoroughly consociational system during its first two decades. From the late 1960s on, although India has remained basically consociational, some of its power-sharing elements have weakened under the pressure of greater mass mobilization. Concomitantly, in accordance with consociational theory, intergroup hostility and violence have increased. Therefore, India is not a deviant case for consociational theory but, instead, an impressive confirming case."}

        //Making empty map
        mp := make(map[string]int)

        //Initializing MapS struct
        map_p := &MapS{mp}

        //Initializing word whose value is required
        word := "power-sharing"

        //Infinite loop for apply and read
        i := 0
        for {
                //calling apply function
                pmdb_apply(mp, uuid_data.raft_uuid, uuid_data.my_uuid, s.data_str)

                //calling pmdb_read which returns count of given word
                res_cnt := pmdb_read(pointer.Save(map_p),uuid_data.raft_uuid, uuid_data.my_uuid, word)
                fmt.Println("Count of word => ",word, ":", res_cnt)
                i++
        }

        /*
        //printing map of (word:counts)
        for i,j := range mp{
                fmt.Println(i,"==>",j)
                }
        */

}

func pmdb_read(data unsafe.Pointer, raft_uuid string, my_uuid string, str string)int{
   fmt.Println("In pmdb read")

   f := pointer.Restore(data).(*MapS)

   //Getting value for key as string
   count := f.my_map[str]

   //Check for value of count
   if count == 0 {
        fmt.Println("Given word is not found!")
    }
   return count
}


func pmdb_apply(wordCountMap map[string]int, raft_uuid string, my_uuid string, str string){

    fmt.Println("In apply function")
    c := strings.Split(str, ",")
    justString := strings.Join(c," ")
    res := strings.Replace(justString, ".", " ",-1)
    res2 := strings.Replace(res, "(", " ",-1)
    data_str := strings.Replace(res2, ")", " ",-1)
    words := strings.Split(data_str, " ")

    for _,word := range words{
        wordCountMap[word]++
    }

}

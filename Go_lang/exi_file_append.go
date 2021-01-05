package main

import (
    "fmt"
    "io/ioutil"
    "os"
)

func main() {

    //mydata := []byte("All the data I wish to write to a file\n")

    // the WriteFile method returns an error if unsuccessful
    //err := ioutil.WriteFile("sample1.txt", mydata, 0777)
    // handle this error
    //if err != nil {
    //    // print it out
    //    fmt.Println(err)
    //}

    data, err := ioutil.ReadFile("exi_sample.txt")
    if err != nil {
        fmt.Println(err)
    }

    fmt.Print(string(data))

    f, err := os.OpenFile("exi_sample.txt", os.O_APPEND|os.O_WRONLY, 0600)
    if err != nil {
        panic(err)
    }
    defer f.Close()

    if _, err = f.WriteString("Date is : 05/01/2021\n"); err != nil {
        panic(err)
    }

    data, err = ioutil.ReadFile("exi_sample.txt")
    if err != nil {
        fmt.Println(err)
    }
    fmt.Print(string(data))

}

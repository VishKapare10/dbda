package main

import (
        //"bufio"
        "encoding/csv"
        "fmt"
        "io"
        "log"
        "os"
        "reflect"
        //"ZomatoAppLib/app_libs"
)

//app_structure definition
type Zomato_data_app struct {
        restaurant_id string //unique key
        restaurant_name string
        city string
        cuisines string
        ratings_text string
        votes string
}

func load_data_and_write(filename string){

        // Open the file
        csvfile, err := os.Open(filename)
        if err != nil {
                log.Fatalln("Couldn't open the csv file", err)
        }

        // Parse the file
        r := csv.NewReader(csvfile)
        //r := csv.NewReader(bufio.NewReader(csvfile))

        // Iterate through the records
        for {
                // Read each record from csv
                record, err := r.Read()
                if err == io.EOF {
                        break
                }
                if err != nil {
                        log.Fatal(err)
                }

                fmt.Printf("Rest_id: %s Rest_name: %s City: %s Cousines: %s Ratings_text: %s Votes: %s \n", record[0], record[1], record[2], record[3], record[4], record[5])
                //fill the struture
                req_dict := Zomato_data_app {
                                restaurant_id: record[0],
                                restaurant_name: record[1],
                                city: record[2],
                                cuisines: record[3],
                                ratings_text: record[4],
                                votes: record[5],
                        }

                fmt.Println("Type of req_dict = ", reflect.TypeOf(req_dict))
                fmt.Println("Type of record =", reflect.TypeOf(record))
                fmt.Println(len(record))
        }

}

func main() {

        ///Get operation to be performed from cmdline
        ops := os.Args[1]

        fmt.Println("Operation to be performed:", ops)

        if ops == "write"{
                load_data_and_write("zomato_data.csv")
        } else {
                fmt.Println("In read")
        }
}

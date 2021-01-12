package main

/*
#include "stdio.h"
#pragma pack(1)
typedef struct{
        int num;
        char str[5];
}packed;

packed PackedInit(){
        packed p;
        p.num = 1000;
        p.str[0] = 'h';
        p.str[1] = 'o';
        p.str[2] = 'l';
        p.str[3] = 'o';
        p.str[4] = 'n';
        return p;
}

*/
import "C"
import (
        "bytes"
        "encoding/binary"
        "fmt"
        "unsafe"
)

//GoPack is the go version of the c packed structure
type GoPack struct {
        num int32
        e [5]uint8
}

func (g *GoPack) Unpack(i *C.packed) {
        cdata := C.GoBytes(unsafe.Pointer(i), C.sizeof_packed)
        buf := bytes.NewBuffer(cdata)
        binary.Read(buf, binary.LittleEndian, &g.num)
        binary.Read(buf, binary.LittleEndian, &g.e)
}

func main() {
        packed := C.PackedInit()
        gopacked := GoPack{}
        gopacked.Unpack(&packed)
        fmt.Printf("num: %d\nStr: %s\n", gopacked.num, string(gopacked.e[:]))
}

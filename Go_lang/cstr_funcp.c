#include<stdio.h>

typedef struct structdemo {
    int(*substract)(void*,int a ,int b);
    void(*display)(void*);
} structdemo;

int substract(void* self, int a, int b) {
    return a-b;
}

void display(void* self){
   printf("In display method of structure pointer\n");

}

structdemo initializeStruct() {
    structdemo demo1;
    demo1.substract = &substract;
    demo1.display = &display;
    return demo1;
}

int start(a,b)
{
    structdemo p = initializeStruct();
    printf("Substraction = %i\n", p.substract(&p, a,b));
    p.display(&p);
    return 0;
}

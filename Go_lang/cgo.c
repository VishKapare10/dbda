#include<stdio.h>


void display_msg() {
    printf("In display msg method!\n");
}

void print(int a)
{
    printf("Value of a is %d\n", a);
}


int add_integers(int a, int b) {
  void (*fun_ptr)(int) = &print;
  (*fun_ptr)(1500);
  return a+b;
}

#include <stdio.h>

typedef int SYMBOL;

extern SYMBOL __first_pointer;
extern SYMBOL __second_pointer;

int main(int argc, char **argv){
    void(*t1)(void) = (void(*)(void))&__first_pointer;
    void(*t2)(void) = (void(*)(void))&__second_pointer;

    t1();
    t2();

    printf("first: %p\nsecond: %p\n",
            &__first_pointer, &__second_pointer);
    return 0;
}

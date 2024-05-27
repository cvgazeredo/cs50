#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    //to print pointer use %p
    printf("%p\n", p);

    //or we can simply do that:
    int m = 50;
    printf("%p\n", &m);

    int o = 50;
    int *q = &o;
    //the current address of 'o':
    printf("%p\n", q);
    //the value of 'o':
    printf("%i\n", o);

    //OR:
    int w = 50;
    int *r = &w;
    //the current address of 'w':
    printf("%p\n", r);
    //it like go to the value of 'w':
    printf("%i\n", *r);

}
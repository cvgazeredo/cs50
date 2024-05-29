
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n; //guarda o endereco da memoria onde esta armazenado o numero 50
    printf("%p\n", p); //contem o endereco da memoria em si
    printf("%i\n", *p); // contem o valor dentro do endereco

    n = 60;
    printf("%i\n", *p);



}
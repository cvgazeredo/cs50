#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("n: ");

    //If n is even (par) - % é o resto da equacao de divisao
    if (n % 2 == 0)
    {
        printf("even\n");
    }
    else
    {
        printf("odd\n");
    }

}
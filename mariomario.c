#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int altura;
    do
    {
        altura = get_int("Height: ");
    }
    while (altura < 1 || altura >= 8);

    for (int fila = 0; fila < altura; fila++)
    {
        for (int coluna = 0; coluna <= fila; coluna++)
        {
            printf("#");
        }
        printf("\n");
    }

}
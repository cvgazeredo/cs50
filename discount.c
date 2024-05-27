#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float regular = get_float("Regular price: ");
    float sale = regular * .85;
    printf("Sale Price: %.2f\n", sale);
}
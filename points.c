#include <cs50.h>
#include <stdio.h>

int main(void)
{
    const int MINE = 2;
    int point = get_int("How many points did you lose? ");

    if (point < MINE)
    {
        printf("You lost fewer points than me.\n");
    }
    else if (point > MINE)
    {
        printf("You lost more points than me.\n");
    }
    else
    {
        printf("You lost as same point as me. \n");
    }
}
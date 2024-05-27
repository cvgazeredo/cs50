#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Width: ");
    }
    // Pq n pode ser negativo
    while (n < 1; n <= 8 );
    // For each row
    for (int i = 0; i < n; i++)
    {
        // For each column
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }

        // Move to next row
        printf("\n");
    }

}
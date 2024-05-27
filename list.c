#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    //int list[3];

    //list[0] = 1;
    //list[1] = 2;
    //list[2] = 3;

    //for (int i = 0; i < 3; i++)
    //{
    //    printf("%i\n", list[i] );
    //}

    // int list[3];  //this puts the MEMORY on the STACK automatically for me; its permanent!!

    int *list = malloc(3 * sizeof(int)); // this is creating an array of size 3, but putting it
                                        // on the HEAP;
    if (list == NULL) //if it returns 1, the computer is out of memory, and will quit!
    {                   // ITS IMPORTANT TO CHECK!
        return 1;
    }

    list[0] = 1; //Its ok to use it now like and array we are confortable seeing -
    list[1] = 2; // o pc vai fazer a aritmetica pra mim e achar the first location, the second and third
    list[2] = 3;

    //Time pass and I want to put one more value in the array
    // I want to add one more value dynamically
// Is this would work? Not really
//    list = malloc(4 * sizeof(int));
//    list [3] = 4; //I want to start an array with of size 3, with 1,2,3 and add a number 4 to it.

// I have to give a temporary variable:
   int *tmp = malloc(4 * sizeof(int));
   // So I will ask the computer a completely different chunk of memory of size 4
   if (tmp == NULL) // thats a safety check 'if there is no memory, free and quit'
   {
       free(list);
       return 1;
   }
   for (int i = 0; i < 3; i++) //I am copying the values of the old list into the new list
   {
       tmp[i] = list[i]; //It will copy all of the memory from one to the other
   }

   tmp[3] = 4; //I will add my new number at the end of the new list

   free(list); //I have to free the old list and then change the new values!
                //Remeber I am freeing the address in the variable, not the variables!
   list = tmp; //I will remember to the old list, whats the address of this new chunk memory

   for(int i = 0; i < 4; i++)
   {
       printf("%i\n", list[i]);
   }
    free(list); // I have to free again
    return 0;
    //CHECK REALLOC.C TO SEE A NEW HANDY WAY OF DOING THIS!!!!!!
}
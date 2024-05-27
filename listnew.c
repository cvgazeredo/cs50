#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(void)
{
    //List of size 0
    node *list = NULL;

    //Add a number to list
    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next = NULL;

    //Update list to point to new node
    list = n;

    //Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->number = 2;
    n->next = NULL;
    list->next = n;

    //Add a number to list
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n;

    //Print the numbers
    //A for loop that uses:
    //    node* variable inicialized to the list itself (its like 'pointing my finger at the number 1 node)
    // I will keep doing this so long as tmp does not equals NULL(its like asking if tmp not equal NULL?)
    //      Hopefully it will not equals NULL since i am pointing at a valid node that is the number 1 node
    //     (NULL will be when we get to the end of the list, obviously)
    // And on each iteration of this loop i will update tmp to be whatever tmp->next is
    // (Its like I started this tmp variable, I follow the arrow and go to the number field they're in)
    // What do I then do?
    // The for loop says, change the tmp to be whatever is at tmp, by following the arrow and grabbing
    // the next field
    for (node *tmp = list; tmp != NULL; tmp  = tmp->next)
    {
        printf("%i\n", tmp->number);
        // I will print out the number in this temporary variable
    }

    //Free list
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return 0;
}
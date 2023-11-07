#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */

size_t num_od_nodes(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        current = current->next;
        n++;
    }

    return (n);
}


/**
 * is_palindrome - a function in C that checks if a
 * singly linked list is a palindrome.
 * @head: address of the first item in the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int n = 0, i = 0, *arr;
	listint_t *current, *temp;

	current = *head;
	temp  = *head;

	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	arr = malloc(sizeof(int) * n);
	while(temp != NULL)
	{
		arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	for (i = 0; i < n; i++)
	{
		if (arr[i] != arr[n - 1 - i])
			return (0);
	}
	return (1);
}


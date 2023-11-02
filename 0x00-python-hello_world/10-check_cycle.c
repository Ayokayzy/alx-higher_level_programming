#include "lists.h"

/**
 * check_cycle - a function in C that checks if a
 * singly linked list has a cycle in it.
 * @list: the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	while (current->next != NULL)
	{
		if (current->next == list)
			return (1);

		current = current->next;
	}

	if (current->next == list)
		return (1);
	else
		return (0);
}

#include "lists.h"

/**
 * check_cycle - a function in C that checks if a
 * singly linked list has a cycle in it.
 * @list: the head of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp, *current = list;

	if (list == NULL)
		return (0);

	temp = list->next;

	if (temp == NULL)
		return (0);

	while (current->next != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}

	return (0);
}

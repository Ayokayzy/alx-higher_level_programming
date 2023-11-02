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

	while (current != temp)
	{
		if (temp->next == NULL || temp->next->next == NULL)
			return (0);
		current = current->next;
		temp = temp->next->next;
	}

	return (1);
}

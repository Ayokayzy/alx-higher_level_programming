#include "lists.h"

/**
 * insert_node - a function that inserts a number into a
 * sorted singly linked list.
 * @head: the beginning of the list
 * @number: the data to be inserted into the list
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node, *temp;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	current = *head;

	if (current == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
	}
	else
	{
		while (current->next != NULL)
		{
			/* check if the next index is where we want to insert our new node */
			if (number > current->n)
			{
				temp = current;
				current = current->next;
				if (number <= current->n)
				{
					new_node->next = current;
					temp->next = new_node;
					break;
				}
				current = temp;
				current = current->next;
			}
		}
		if (number > current->n)
		{
			current->next = new_node;
			new_node->next = NULL;
		}
		else
		{
			new_node->next = current;
			temp->next = new_node;
		}
	}
	return (new_node);
}

#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: list head
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *future;

	if (!list)
		return (0);

	current = list;
	future = list->next;

	while (current && future && future->next)
	{
		if (current == future)
			return (1);

		current = current->next;
		future = future->next->next;
	}

	return (0);
}

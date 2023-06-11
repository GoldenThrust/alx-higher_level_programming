#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	listint_t *current = *head, *future = *head;
	listint_t *prev = NULL, *cur, *next;
	listint_t *start = *head, *end;

	while (future->next != NULL && future->next->next != NULL)
	{
		current = current->next;
		future = future->next->next;
	}

	cur = current->next;

	while (cur != NULL)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}

	end = prev;

	while (start && end)
	{
		if (start->n != end->n)
			return (0);

		start = start->next;
		end = end->next;
	}

	return (1);
}


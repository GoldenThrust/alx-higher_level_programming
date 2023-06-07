#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the list head
 * @number: number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (!node || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new_node->next = node->next;
	node->next = new_node;

	return (node_node);
}

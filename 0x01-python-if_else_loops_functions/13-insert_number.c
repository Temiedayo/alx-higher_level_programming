#include "lists.h"
#include "stdlib.h"
#include "stddef.h"
/**
 * insert_node - Inputs number into a sorted singly-linked list.
 * @head: Head of linked list.
 * @number: Number to be inserted.
 *
 * Return: NULL, if it fails.
 * Otherwise - Pointer to new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;
if (node == NULL || node->n >= number)
{
new->next = node;
*head = new;
return (new);
}
while (node && node->next && node->next->n < number)
node = node->next;
new->next = node->next;
node->next = new;
return (new);
}

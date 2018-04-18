#include "lists.h"

/**
 * is_palindrome - function to call check_pal to see if list is palindrome
 * @head: ptr to the beginning of the list
 * Return: 0 if not palindrome else 1
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - function to check if the list is palindrome
 * @head: ptr to the beginning of the list
 * @last: ptr to the end of the list
 * Return: 0 if not palindrom else 1
 */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

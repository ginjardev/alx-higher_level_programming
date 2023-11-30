#include "lists.h"

/**
 * check_cycle - Check if a list has a cycle or not.
 * @list: Pointer to the head of the list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = second = list;

	while (first && second && second->next)
	{
		first = first->next;
		second = second->next->next;
		if (first == second)
			return (1);
	}
	return (0);
}

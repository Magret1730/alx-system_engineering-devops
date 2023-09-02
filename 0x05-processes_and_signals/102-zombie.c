#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite while loop to pause the process by 1 second
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - program that creates 5 zombie processes.
 * Return: 0
 */
int main(void)
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork(); /*child process created*/
		if (child_pid == 0) /*This is the child process*/
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			exit(0);
		}
	}
	if (child_pid > 0) /*This is the parent process*/
		infinite_while();
	else
		return (1);
	return (0);
}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

/**
 * infinite_while- functtion for an infinite loop
 * Return: integer value
*/
int infinite_while(void)
{	/*infinite loop*/
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main- main entry of the function
 * Return: integer value
*/
int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID:%d\n", pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_while();
	return (EXIT_SUCCESS);
}

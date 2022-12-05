#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include "libft.h"

typedef struct s_elves
{
    int calories;
    struct s_elves *next;
    struct s_elves *prev;
} t_elves;

t_elves *new_elf(int calories)
{
    t_elves *new_elf;

    new_elf = (t_elves *)malloc(sizeof(t_elves));
    ft_bzero(new_elf, sizeof(t_elves));
    new_elf->calories = calories;

    return (new_elf);
}

void add_elf(t_elves **first, int calories)
{
    t_elves *curr;
    t_elves *prev;
    t_elves *new;

    curr = *first;
    prev = NULL;
    if (!curr)
    {
        curr = new_elf(calories);
        *first = curr;
    }
    else
    {
        new = new_elf(calories);
        while (curr)
        {
            if (calories < curr->calories)
            {
                new->next = curr;
                new->prev = curr->prev;
                curr->prev = new;
                if (curr == *first)
                    *first = new;
                return ;
            }
            prev = curr;
            curr = curr->next;
        }
        prev->next = new;
        new->prev = prev;
    }
}

int main()
{
    int fd;
    char *line;
    size_t n_read;
    t_elves *elves = NULL;
    int curr_calories = 0;

    n_read = 0;
    if ((fd = open("./resources/day01.csv", O_RDONLY)) < 0)
        return (-1);

    while ((n_read = get_next_line(fd, &line)) > 0)
    {
        if (strlen(line) == 0)
        {
            add_elf(&elves, curr_calories);
            curr_calories = 0;
        }
        else
            curr_calories += ft_atoi(line);
    }
    int max_cals = 0;
    while(elves->next)
        elves = elves->next;
    printf("%d %d\n", elves->calories, elves->calories + elves->prev->calories + elves->prev->prev->calories);
    return (0);
}
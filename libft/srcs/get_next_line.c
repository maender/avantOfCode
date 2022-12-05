/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/16 17:17:04 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/24 10:07:29 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include "libft.h"

#define BUFF_SIZE 4096

int			res(char **line, char *old)
{
	char	*eol;

	eol = ft_strchr(old, '\n');
	if (NULL != eol)
	{
		*eol = '\0';
		*line = ft_strdup(old);
		ft_memmove(old, &eol[1], ft_strlen(&eol[1]) + 1);
		return (1);
	}
	if (0 < ft_strlen(old))
	{
		*line = ft_strdup(old);
		*old = '\0';
		return (1);
	}
	ft_strdel(&old);
	return (0);
}

int			gnl(const int fd, char *buff, char **old)
{
	char	*tmp;
	int		ret;

	tmp = NULL;
	while (!ft_strchr(*old, 10))
	{
		ret = read(fd, buff, BUFF_SIZE);
		if (ret == -1)
			return (-1);
		if (0 == ret)
			break ;
		buff[ret] = '\0';
		tmp = ft_strjoinfree(*old, buff);
		*old = tmp;
		if (!ft_isprint(**old))
		{
			ft_strdel(old);
			return (-1);
		}
	}
	return (1);
}

int			get_next_line(const int fd, char **line)
{
	static char	*old = NULL;
	char		buff[BUFF_SIZE + 1];

	ft_bzero(buff, BUFF_SIZE + 1);
	if (NULL == line || fd < 0 || BUFF_SIZE <= 0)
		return (-1);
	if (NULL == old)
		old = ft_strnew(0);
	if (gnl(fd, buff, &old) < 0)
		return (-1);
	return (res(line, old));
}

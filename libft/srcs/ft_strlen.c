/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/03 22:16:10 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/24 10:05:46 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdint.h>

static int64_t	detectnull(int64_t s)
{
	return ((s - 0x0101010101010101) & ~s & 0x8080808080808080);
}

size_t			ft_strlen(const char *s)
{
	char	*str;
	int		i;

	str = NULL;
	i = 0;
	if (!s)
		return (0);
	str = (char *)s;
	while (str[i] && (uintptr_t)str & 7)
		i++;
	while (!(detectnull((int64_t)str[i])))
		i += sizeof(int64_t);
	while (str[i])
		i++;
	return (&str[i] - s);
}

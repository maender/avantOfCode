/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_splitwhitespaces.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/02/24 19:01:30 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:48:14 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

static size_t	ft_wc(char const *s)
{
	size_t	i;
	size_t	j;

	i = 0;
	j = 0;
	while (s[i])
	{
		while ((s[i] == ' ' || s[i] == '\t') && s[i])
			i++;
		if ((s[i] != ' ' && s[i] != '\t'))
			j++;
		while ((s[i] != ' ' && s[i] != '\t') && s[i])
			i++;
	}
	return (j);
}

static size_t	ft_lc(char const *s)
{
	size_t	i;

	i = 0;
	while (s[i] && (s[i] != ' ' && s[i] != '\t'))
		i++;
	return (i);
}

char			**ft_splitwhitespaces(char const *s)
{
	int		i;
	int		j;
	char	**arr;

	i = 0;
	j = 0;
	if (!s)
		return (NULL);
	if (!(arr = (char**)malloc(sizeof(char*) * ft_wc(s) + 1)))
		return (NULL);
	while (s[i])
	{
		while ((s[i] == ' ' || s[i] == '\t') && s[i])
			i++;
		if (s[i])
		{
			if (!(arr[j] = ft_strsub(s, i, ft_lc(s + i))))
				return (ft_free_arr((void**)arr) ? NULL : NULL);
			while ((s[i] != ' ' && s[i] != '\t') && s[i])
				i++;
			j++;
		}
	}
	arr[j] = NULL;
	return (arr);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/08 15:41:16 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:51:09 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*new;
	size_t	i;
	size_t	pos;

	if (!s1 && !s2)
		return (NULL);
	if (!(new = ft_memalloc(ft_strlen(s1) + ft_strlen(s2) + 1)))
		return (NULL);
	i = 0;
	pos = 0;
	while (s1[i])
		new[pos++] = s1[i++];
	i = 0;
	while (s2[i])
		new[pos++] = s2[i++];
	new[pos] = '\0';
	return (new);
}

char	*ft_strjoinfree(char *s1, char const *s2)
{
	char	*new;
	size_t	i;
	size_t	pos;

	new = NULL;
	if (!s1 || !s2)
		return (s1 ? ft_strdup(s1) : ft_strdup((char*)s2));
	if (!(new = ft_memalloc(ft_strlen(s1) + ft_strlen(s2))))
		return (NULL);
	i = 0;
	pos = 0;
	while (s1[i])
		new[pos++] = s1[i++];
	i = 0;
	while (s2[i])
		new[pos++] = s2[i++];
	new[pos] = '\0';
	ft_strdel(&s1);
	return (new);
}

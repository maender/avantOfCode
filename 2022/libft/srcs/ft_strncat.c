/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/10/07 12:37:19 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:52:15 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strncat(char *s1, const char *s2, size_t n)
{
	char	*tmp;
	size_t	i;
	size_t	j;

	tmp = s1;
	j = ft_strlen(s1);
	i = 0;
	while (s2[i] && n--)
	{
		tmp[j++] = s2[i++];
	}
	tmp[j] = '\0';
	return (s1);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/07 20:24:52 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:51:54 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	size_t	n;
	char	*new;

	n = 0;
	if (!s || !f)
		return (0);
	if (!(new = (char*)ft_memalloc(ft_strlen(s) + 1)))
		return (NULL);
	if (s)
	{
		while (s[n])
		{
			new[n] = f(n, s[n]);
			n++;
		}
	}
	return (new);
}

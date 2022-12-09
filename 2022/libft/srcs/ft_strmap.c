/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/07 20:12:23 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:51:50 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmap(char const *s, char (*f)(char))
{
	size_t	n;
	char	*new;

	n = 0;
	if (!s || !f)
		return (0);
	if (!(new = ft_strnew(ft_strlen(s))))
		return (NULL);
	while (s[n])
	{
		new[n] = f(s[n]);
		n++;
	}
	return (new);
}

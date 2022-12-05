/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/08 10:47:42 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:45:56 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	*nsrc;
	unsigned char	nc;

	nsrc = (unsigned char*)s;
	nc = (unsigned char)c;
	while (n--)
	{
		if (*nsrc == nc)
			return (nsrc);
		nsrc++;
	}
	return (NULL);
}

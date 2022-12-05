/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/10/07 12:39:16 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:52:22 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strncpy(char *dst, const char *src, size_t len)
{
	size_t x;

	x = 0;
	while (x < len && src[x] != '\0')
	{
		dst[x] = src[x];
		x++;
	}
	while (x < len)
	{
		dst[x] = '\0';
		x++;
	}
	dst[x] = '\0';
	return (dst);
}

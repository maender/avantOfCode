/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/30 13:45:11 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:46:08 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dst, const void *src, size_t len)
{
	char		*ndst;
	const char	*nsrc;

	ndst = (char*)dst;
	nsrc = (const char*)src;
	if (ndst > nsrc)
	{
		ndst += len - 1;
		nsrc += len - 1;
		while (len--)
			*ndst-- = *nsrc--;
	}
	else
	{
		while (len-- > 0)
			*ndst++ = *nsrc++;
	}
	return (dst);
}

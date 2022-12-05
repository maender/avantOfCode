/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_realloc.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/12 17:41:28 by sdincbud          #+#    #+#             */
/*   Updated: 2018/11/12 17:49:14 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include "libft.h"

void	*ft_realloc(void *src, size_t size)
{
	void *out;

	if (!src && size)
	{
		if (!(out = malloc(size)))
			return (NULL);
		return (out);
	}
	else if (!size && src)
	{
		free(src);
		src = NULL;
		return (NULL);
	}
	else
	{
		if (!(out = malloc(size)))
			return (NULL);
		ft_memcpy(src, out, size);
		free(src);
		src = (NULL);
		return (out);
	}
}

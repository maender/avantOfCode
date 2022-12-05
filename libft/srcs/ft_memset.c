/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/08 10:47:42 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:46:14 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *b, long long int c, size_t len)
{
	size_t	i;
	char	*d;

	i = 0;
	d = (char*)b;
	while (i < len)
	{
		d[i] = c;
		i++;
	}
	return (b);
}

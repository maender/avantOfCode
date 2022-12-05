/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/09/04 12:03:08 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:55:15 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	unsigned char	*ns1;
	unsigned char	*ns2;
	size_t			i;

	i = 0;
	if (!n)
		return (0);
	ns1 = (unsigned char*)s1;
	ns2 = (unsigned char*)s2;
	while (ns1[i] && ns1[i] == ns2[i] && i < n - 1)
	{
		i++;
	}
	return (ns1[i] - ns2[i]);
}

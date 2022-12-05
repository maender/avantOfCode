/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/10/10 15:32:05 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:43:58 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char		*ft_itoa(int n)
{
	char	*itoa;
	long	nbr;
	int		end;

	if (!(itoa = ft_strnew((size_t)ft_snbrlen(n))))
		return (NULL);
	nbr = n;
	end = ft_snbrlen(n);
	itoa[end--] = '\0';
	if (n < 0)
	{
		nbr = -nbr;
		itoa[0] = '-';
	}
	if (n == 0)
		*itoa = '0';
	while (nbr)
	{
		itoa[end] = nbr % 10 + '0';
		nbr /= 10;
		end--;
	}
	return (itoa);
}

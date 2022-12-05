/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/12 21:28:43 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:53:01 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrev(char *str)
{
	int		a;
	int		b;
	char	tmp;

	a = 0;
	b = 0;
	if (!str)
		return (NULL);
	while (str[b] != '\0')
		b++;
	b -= 1;
	while (b >= a)
	{
		tmp = str[b];
		str[b] = str[a];
		str[a] = tmp;
		a++;
		b--;
	}
	return (str);
}

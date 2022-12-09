/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnsplit.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/10/08 10:38:01 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:56:17 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

char	**ft_strnsplit(char const *s, size_t len, size_t lentwo)
{
	int		i;
	int		j;
	char	**arr;

	i = 0;
	j = 0;
	if (!s || len == 0 || lentwo == 0)
		return (NULL);
	if (!(arr = (char**)malloc(sizeof(char*) * (len + 1))))
		return (NULL);
	while (len--)
	{
		if (!(arr[j] = ft_strsub(s, i, lentwo)))
			return (ft_free_arr((void**)arr) ? NULL : NULL);
		j++;
		i += lentwo;
	}
	arr[j] = NULL;
	return (arr);
}

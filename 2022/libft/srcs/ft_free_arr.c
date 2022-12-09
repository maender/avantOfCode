/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_free_arr.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: maabou-h <maabou-h@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/02/21 14:30:04 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 19:28:05 by maabou-h         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

int	ft_free_arr(void **arr)
{
	int x;

	x = 0;
	while (arr[x])
	{
		ft_strdel((char**)&arr[x]);
		x++;
	}
	free(arr);
	return (0);
}

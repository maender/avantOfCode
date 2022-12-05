/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_free_matrix.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/04/29 15:43:14 by sdincbud          #+#    #+#             */
/*   Updated: 2019/06/15 03:43:21 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <stdlib.h>

void	ft_free_matrix(void **m, size_t len)
{
	int	i;

	i = -1;
	while (++i < (int)len)
	{
		ft_memdel((void**)&m[i]);
	}
	if (m)
		free(m);
}

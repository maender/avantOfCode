/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/17 19:01:35 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:31:30 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int		ft_sqrt(int nb)
{
	int square;
	int max;

	square = 0;
	max = nb >> 1;
	while (square < max)
	{
		if ((square * square) == nb)
			return (square);
		square++;
	}
	return (0);
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnequ.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/07 22:00:25 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:52:32 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

int	ft_strnequ(char const *s1, char const *s2, size_t n)
{
	size_t	i;

	i = 0;
	if (!s1 || !s2)
		return (0);
	if ((ft_strlen(s1) == 0 && ft_strlen(s2) == 0) || !n)
		return (1);
	while (i < n - 1 && s1[i] == s2[i] && s1[i])
	{
		i++;
	}
	return (s1[i] == s2[i]);
}

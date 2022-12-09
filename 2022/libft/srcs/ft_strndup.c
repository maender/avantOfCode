/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strndup.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: maabou-h <maabou-h@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/10 21:04:38 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/16 13:55:30 by maabou-h         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strndup(const char *s1, size_t n)
{
	char	*new;

	if (!s1 || !n)
		return (NULL);
	if (!(new = (char*)ft_strnew(n)))
		return (NULL);
	return (ft_strncpy(new, s1, n));
}

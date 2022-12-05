/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strsub.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/07 22:03:45 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:53:20 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strsub(char const *s, unsigned int start, size_t len)
{
	char	*ns;
	int		i;

	if (!s)
		return (0);
	if (!(ns = (char*)ft_memalloc(len + 1)))
		return (NULL);
	i = 0;
	while (len-- && s[start])
		ns[i++] = s[start++];
	return (ns);
}

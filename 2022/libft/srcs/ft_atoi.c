/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2018/11/06 22:50:12 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/23 20:24:45 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(const char *str)
{
	int		i;
	int		neg;
	long	ret;

	i = 0;
	ret = 0;
	neg = 0;
	if (!str || !*str)
		return (0);
	while (str[i] && ((str[i] >= 7 && str[i] <= 13 && str[i] != '\n')
			|| str[i] == ' '))
		i++;
	if (str[i] && str[i] == '-')
		neg = 1;
	if (str[i] && (str[i] == '+' || str[i] == '-'))
		i++;
	while (str[i] && str[i] <= '9' && str[i] >= '0')
	{
		ret *= 10;
		ret += str[i++] - '0';
	}
	return ((neg) ? ((int)-ret) : ((int)ret));
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_snbrlen.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: sdincbud <sdincbud@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/02/21 13:50:14 by maabou-h          #+#    #+#             */
/*   Updated: 2019/06/15 03:47:40 by sdincbud         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_snbrlen(long long int n)
{
	int intlen;

	intlen = 1;
	n = (n < 0) ? -n : n;
	intlen = (n < 0) ? intlen + 1 : intlen;
	while (n > 9)
	{
		intlen++;
		n /= 10;
	}
	return (intlen);
}

"""

Find the prime factors for a given number.

"""


def prime_factors(number):

    factor_list = []

    divisor = 2

    while number >= divisor:

        if number % divisor == 0:
            factor_list.append(divisor)
            number = number / divisor
        else:
            divisor += 1

    return factor_list

print(prime_factors(34552))
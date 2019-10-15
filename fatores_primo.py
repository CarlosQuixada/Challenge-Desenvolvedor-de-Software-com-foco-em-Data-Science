"""
Qualquer número inteiro positivo pode ser representado pelo produto de potências de números primos (os chamados fatores primos).
Por exemplo o número 6 pode ser representado pelo produto do números primos 2 x 3.
"""


def identify_prime_factor(number):
    factor = 2
    prime_factors = []

    while number > 1:
        if number % factor == 0:
            number = number / factor
            prime_factors.append(factor)
        else:
            factor += 1

    return prime_factors


number = int(input('Entre com o número: '))

response = identify_prime_factor(number)

print(response)

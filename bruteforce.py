import math

# Hardcoded all primes up to 100
# via https://en.wikipedia.org/wiki/List_of_prime_numbers


def hardcoded(upto=100):
    assert upto <= hardcoded.max
    # fmt: off
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    # fmt: on
    return [p for p in primes if p <= upto]


hardcoded.max = 100


# Brute-force solutions that check every possible factor


def primes_exhaustive(upto=100):
    primes = []
    for number in range(2, upto + 1):
        if not any(number % factor == 0 for factor in range(2, number)):
            primes.append(number)
    return primes


def primes_sqrt(upto=100):
    primes = []
    for number in range(2, upto + 1):
        max_factor = int(math.sqrt(number))
        if not any(number % factor == 0 for factor in range(2, max_factor + 1)):
            primes.append(number)
    return primes

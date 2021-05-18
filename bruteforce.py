import math


def primes_exhaustive(upto=100):
    primes = []
    for number in range(2, upto):
        if not any(number % factor == 0 for factor in range(2, number)):
            primes.append(number)
    return primes


def primes_sqrt(upto=100):
    primes = []
    for number in range(2, upto):
        max_factor = int(math.sqrt(number))
        if not any(number % factor == 0 for factor in range(2, max_factor+1)):
            primes.append(number)
    return primes


if __name__ == "__main__":
    print(primes())
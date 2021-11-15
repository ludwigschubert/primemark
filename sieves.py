# Variable names: see https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

# In sieve-style algorithms, I use the following naming conventions:
# [upto] N; _up to_ how many integers to consider in the search for primes
# [sand] the initial set of natural numbers 1...N
# [grain] an element of `sand`
# [sieve] a number that will help us exclude a number from the primes


def eratosthenes(upto=100):
    # start with a list of the integers from 1 to n, and en empty one
    sand = list(range(1, upto + 1))
    primes = []
    # for each number we take a look
    for index in range(2, len(sand) + 1):
        candidate = sand[index - 1]
        if candidate:  # i.e. if we haven't crossed this number out yet
            primes.append(candidate)
            # cross out every multiple of this prime
            for sieve in range(candidate, upto + 1, candidate):
                sand[sieve - 1] = None
    return primes


def sundaram(upto=100):
    # sundaram sieve computes all primes below 2n + 1, so we want the inverse
    n = (upto - 1) // 2
    # start with a list of the integers from 1 to n
    sand = list(range(1, n + 1))
    # where i, j are natural numbers, 1 <= i <= j
    for i in range(1, n + 1):
        immediately_out_of_bounds = True
        for j in range(1, n + 1):
            # and i + j + 2ij <= n
            sieve = i + j + 2 * i * j
            if sieve > n:
                break
            else:
                immediately_out_of_bounds = False
            sand[sieve - 1] = None  # we remove that number.
        if immediately_out_of_bounds:
            break
    # the remaining numbers are doubled and incremented by one,
    primes = [2 * grain + 1 for grain in sand if grain is not None]
    # giving a list of the odd prime numbers (i.e., all primes except 2)
    if upto >= 2:
        primes = [2] + primes
    return primes


if __name__ == "__main__":
    print(eratosthenes())
    print(sundaram())

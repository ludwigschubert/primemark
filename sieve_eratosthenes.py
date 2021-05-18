# Variable names: see https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def prime_sieve(upto=100):
    sand = list(range(1, upto+1))
    primes = []
    for index in range(2, len(sand)):
        candidate = sand[index-1]
        if candidate is None:
            continue
        primes.append(candidate)
        for sieve in range(candidate, upto, candidate):
            sand[sieve-1] = None
    return primes


if __name__ == "__main__":
    print(primes())
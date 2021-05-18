import pytest

import bruteforce
import sieve_eratosthenes


primes_up_to_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

algorithms = [
    bruteforce.primes_exhaustive,  # careful: exponential runtime
    bruteforce.primes_sqrt,  # careful: exponential runtime
    sieve_eratosthenes.prime_sieve
]

@pytest.mark.parametrize("algorithm", algorithms)
def test_correctness(algorithm):
    result = algorithm(100)
    assert result == primes_up_to_100

@pytest.mark.parametrize("algorithm", algorithms)
def test_runtime(benchmark, algorithm):
    # stay around 1_000 if tested algorithm has exponential runtime; slow otherwise
    benchmark(algorithm, 1_000)

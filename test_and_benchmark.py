import pytest

import bruteforce
import sieves

algorithms = [
    bruteforce.primes_exhaustive,  # careful: exponential runtime
    bruteforce.primes_sqrt,  # careful: exponential runtime
    sieves.eratosthenes,
    sieves.sundaram,
]


@pytest.mark.parametrize("algorithm", algorithms)
def test_correctness(algorithm):
    for upto in range(1, bruteforce.hardcoded.max + 1):
        golden = bruteforce.hardcoded(upto)
        result = algorithm(upto)
        assert result == golden


@pytest.mark.parametrize("algorithm", algorithms)
def test_runtime(benchmark, algorithm):
    # stay around 1_000 if tested algorithm has exponential runtime; slow otherwise
    benchmark(algorithm, 1_000)

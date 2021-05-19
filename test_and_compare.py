from bruteforce import hardcoded
from test_and_benchmark import algorithms


def test_prime_algos_agree_with_hardcoded():
    for N in range(100):
        print(f"Up to {N} first prime numbers:")
        results = {f: f(N) for f in algorithms}
        results[hardcoded] = hardcoded(N)
        for key, value in results.items():
            print(f"\t{key.__name__:17}:\t{value}")
        assert all(result == results[hardcoded] for result in results.values())


if __name__ == "__main__":
    test_prime_algos_agree_with_hardcoded()

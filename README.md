# Prime Number Benchmark

Prime number benchmark suite for Kyan. Add your algorithms as a new file, import it in `test_and_benchmark`, and add it to the `algorithms` list! Your code should expose a function that takes as its only argument the number up to which it should check for prime numbers.

I've added two example files:
* `bruteforce.py` tries every possible factor in `primes_exhaustive()`. In `primes_sqrt()` it only checks factors up to the sqrt of the number we're checking.
* `sieve_eratosthenes.py` implements a standard prime number finding algorithm you learn in school; roughly from the year 200BC. There are other, more complicated sieve-style algorithms — search for sieve of Sundaram (1934) or sieve of Atkin (2003) for newer approaches. These could be fun to implement, too!

# Running

In the folder you checked out this project to, run `poetry install`. That should install dependencies, primarily `pytest-benchmark`. (You can install that manually if poetry doesn't work for you.)

Tests can be run as normal, from VSCode or from the CLI: `python -m pytest .`

# Example results

Name                              [...]   Mean (time in μs)  [...]
----------------------------------[...]----------------------[...]
test_runtime[prime_sieve]         [...]    980.1151 (1.0)    [...]
test_runtime[primes_sqrt]         [...]  5,051.5395 (5.15)   [...]
test_runtime[primes_exhaustive]   [...] 39,739.6182 (40.55)  [...]
----------------------------------[...]----------------------[...]
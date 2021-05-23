# Prime Number Benchmark

Prime number benchmark suite for Kyan. Add your algorithms as a new file, import it in `test_and_benchmark`, and add it to the `algorithms` list! Your code should expose a function that takes as its only argument the number up to which it should check for prime numbers.

I've added two example files:
* `bruteforce.py` tries every possible factor in `primes_exhaustive()`. In `primes_sqrt()` it only checks factors up to the sqrt of the number we're checking.
* `sieve_eratosthenes.py` implements a standard prime number finding algorithm you learn in school; roughly from the year 200BC. There are other, more complicated sieve-style algorithms — search for sieve of Sundaram (1934) or sieve of Atkin (2003) for newer approaches. These could be fun to implement, too!

To see how deep the rabbit hole goes, start with https://en.wikipedia.org/wiki/Sieve_theory.

# Running

In the folder you checked out this project to, run `poetry install`. That should install dependencies, primarily `pytest-benchmark`. (You can install that manually if poetry doesn't work for you.)

Tests can be run as normal, from VSCode or from the CLI: `python -m pytest .`

Running `[poetry run] python visualize.py` produces an ulam spiral visualization in the `results` folder:

![visualization_ulam_spiral](https://user-images.githubusercontent.com/1167977/119270670-c1ef5000-bbf5-11eb-929a-36bc450f32f4.png)


# Developing

I added a couple tools as git pre-commit hooks; managed via the `pre-commit` package.
To install the git hooks after a fresh checkout: `poetry run pre-commit install`. After this, every `git commit` will first run the checks specified in `.pre-commit-config.yaml`; i.e. linting (`pylint`), import sorting (`isort`), and formatting (`black`).

# Example results

Name                              [...]   Mean (time in μs)  [...]
----------------------------------[...]----------------------[...]
test_runtime[prime_sieve]         [...]    980.1151 (1.0)    [...]
test_runtime[primes_sqrt]         [...]  5,051.5395 (5.15)   [...]
test_runtime[primes_exhaustive]   [...] 39,739.6182 (40.55)  [...]
----------------------------------[...]----------------------[...]

<img width="1147" alt="Screen Shot 2021-05-18 at 20 53 08" src="https://user-images.githubusercontent.com/1167977/118715032-0efcac00-b81b-11eb-8688-39988363d402.png">

# D400 (C1) Problem Set 2, Exercise 1
# install the relevant packages
import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "sympy"])

# Import all packages for the exercise 1
import math
import sympy as sp
import random

# 1.1 and 1.2: taylor expansion of sin(0.1) to order 5
def sin_taylor(x_val, order=5):
    x = sp.symbols('x') # define the symbol x
    poly = sp.series(sp.sin(x), x, 0, order + 1).removeO()   # Taylor polynomial of sin(x) around 0, up to and including x^order: x - x^3/6 + x^5/120
    return float(poly.subs(x, x_val)) # return the value of the polynomial at x_val as a float

approx = sin_taylor(0.1)
exact = math.sin(0.1)
print(f"Taylor (order 5): {approx:.5f}")   # check: 0.09983

# 1.3 Primes less than N
def primes_below(N):
    return [n for n in range(2, N)
            if all(n % d != 0 for d in range(2, int(n**0.5) + 1))] # prime number by definition: divisible only by 1 and itself, so check all divisors up to sqrt(n)

# 1.4 First N terms of Recaman's sequence (a0 = 0)
def recaman(N):
    seq = [0]
    for n in range(1, N):
        back = seq[-1] - n
        seq.append(back if back > 0 and back not in seq else seq[-1] + n) # the Recaman sequence is defined recursively: a(n) = a(n-1) - n if positive and not already in the sequence, otherwise a(n) = a(n-1) + n
    return seq[:N]

# 1.5 Numbers in both lists when each is N items long
def common_set(A, B):
    return sorted(set(A) & set(B))

# 1.6 Factor pairs of 362880 (a <= b to avoid duplicates)
n = 362880
def factor_pairs(n):
    return [(a, n // a) for a in range(1, int(n**0.5) + 1) if n % a == 0]

# 1.7 Random walk generator, ends at displacement of 10
def random_walk():
    pos = 0
    yield pos
    while abs(pos) < 10: # continue until the absolute value of the position is less than 10
        pos += random.choice([-1, 1])   # randomly choose to go up and down by 1
        yield pos

###### Test the functions ######
if __name__ == "__main__":
    print(primes_below(30))
    print(recaman(15))
    print(common_set([5 , 2, 3, 4, 1], [3, 4, 5, 6, 7]))
    print(factor_pairs(362880))
    print(list(random_walk()))

# ___author__ = Shanjun.Z
# bye !
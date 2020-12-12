"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""

import math

primes = 1
count = 1

def is_primes(count):
    if count == 1:
        return False
    elif count == 2 or count == 3:
        return True
    elif count < 25:
        if count % 3 == 0:
            return False
        else:
            return True
    else:
        for x in range(3, int(math.sqrt(count) + 1), 2):
            if count % x == 0:
                return False
        return True

while primes < 10001:
    check_primes = is_primes(count)
    if check_primes is True:
        _100001_prime = count
        primes += 1   
    count += 2

print(_100001_prime)
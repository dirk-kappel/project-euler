"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import math, time
prime_sum = 2
find_below = 2000000

# Start time
start_time = time.time()

def is_prime(value):
    for y in range(3, int(math.sqrt(value)+1), 2):
        if math.sqrt(value).is_integer():
            return False
        if value % y == 0:
            return False
    return True

for check_prime in range(1,find_below, 2):
    if check_prime == 1:
        continue
    elif check_prime == 3:
        prime_sum += check_prime
        continue
    elif is_prime(check_prime):
        prime_sum += check_prime

end_time = time.time()
print("The sum of prime numbers below", find_below, "is:", prime_sum)
print("The elapsed program running time was:", end_time - start_time)

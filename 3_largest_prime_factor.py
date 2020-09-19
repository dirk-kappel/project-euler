"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math
number = 600851475143
square_root = int(math.sqrt(number)) + 1

if square_root % 2 == 0:
    square_root = square_root - 1

def is_prime(value):
    for y in range(2, int(value/2)):
        if value % y == 0:
            return False
    return True

for x in range(square_root, 2, -2):
    if number % x == 0:     
        prime_factor = is_prime(x)
        if prime_factor == True:
            print("The largest prime factor of", number, "is", x)
            break
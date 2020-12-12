"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
triplet = 1000
import math

def find_triplet():
    for a in range(1,int(triplet/3)+1):
        for b in range(a+1, int((triplet-a)/2)):
            c = math.sqrt(a**2+b**2)
            if c.is_integer():
                if a + b + c == triplet:
                    print("Pythagorean triplet found for", triplet)
                    print("a=",a,"\nb=",b,"\nc=",int(c))
                    return
    print("No pythogorean triplet was found for", triplet)
    return

find_triplet()

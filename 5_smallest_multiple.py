"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

count = 20
y = True
while y:   
    for x in range(20, 10, -1):
        if count % x != 0:  
            count += 10          
            break
        elif x == 11:
            y = False
            continue
print(count)
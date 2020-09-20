"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

# 3 digit numbers 100-999

largest_product = 999*999
smallest_product = 100*100
found = False

# find the palindromes that could be produced by product of 3 digit numbers
for x in range(largest_product, smallest_product, -1):
    if found == True:
        break
    x_string = str(x)
    list_check = []
    for x_string_list in x_string:
        list_check.append(x_string_list)
# check if the the length is an even number so a palindrome is possible
    if len(list_check) % 2 == 0:
        length = len(list_check)//2
        if x_string[:length] == x_string[length:][::-1]:
            for xyz in range(999, 100, -1):
                if x % xyz == 0 and (100 <= x/xyz <= 999):
                    print(xyz, "x", x//xyz, "=", x)
                    found = True
                    break
        






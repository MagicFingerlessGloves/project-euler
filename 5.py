
##########################################################PROBLEM##########################################################

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?



##########################################################SOLUTION##########################################################

# brute-force approach: start at 20 and check each number until we find one that is divisible by all numbers from 1 to 20. 
def isDivisibleOneToTwenty(n):
    for i in range(1,21):
        if n % i != 0:
            return False
    return True

def brute_force():
    number = 20
    found = False
    while not found:
        number += 20
        if isDivisibleOneToTwenty(number):
            found = True
    return number

# You can also use a less brute-force approach by finding the least common multiple (LCM) of the numbers from 1 to 20.
# which requires a gcd function:

# Very inefficient, it requires a stack so long that it will throw a recursion error and, eventually, a segmentation fault
def gcd_pair_recursive_sub(a, b):
    if a == b:
        return a
    if a > b:
        return gcd_pair_recursive_sub(a - b, b)
    if a < b:
        return gcd_pair_recursive_sub(a, b - a)

# Still inefficient as it is recursive, but it will work because modulo is a lot more efficient than subtraction
def gcd_pair_recursive_mod(a, b):
    if b == 0:
        return a
    return gcd_pair_recursive_mod(b, a % b)

# Iterative version of the gcd function using subtraction, which is better but not the most efficient

# Iterative version of the gcd function using modulo, which is the most efficient
def gcd_pair_iterative_mod(a, b):
    while b:
        a, b = b, a % b
    return a

# Returns the least common multiple of two numbers
def lcm_pair(a,b):
    return((a*b)/gcd_pair_iterative_mod(a,b))

# Returns the least common multiple of a list of numbers
def lcm_list(list_of_integers: list):
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        last = list_of_integers.pop()
        return lcm_pair(last, lcm_list(list_of_integers))

######################################################MAIN##########################################################

result = lcm_list([i for i in range(1, 21)])
print(result)


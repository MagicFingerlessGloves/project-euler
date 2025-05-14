##########################################################PROBLEM###################################################

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

### #####################################################SOLUTION#################################################

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_count = 0
start = 1
while prime_count < 10001:
    if is_prime(start):
        prime_count += 1
    start += 1
print(start-1)
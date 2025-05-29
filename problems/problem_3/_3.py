##################################################################PROBLEM##################################################################
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

#################################################################SOLUTION####################################################
# def largerst_prime_factor(n):
#     candidate = 2
#     while candidate * candidate <= n:
#         if n % candidate == 0:
#             n //= candidate
#         else:
#             candidate += 1
#     return candidate

# def largest_prime_factor(n):
#     factor = 2
#     last_factor = 1
#     while factor * factor <= n:
#         if n % factor == 0:
#             last_factor = factor
#             n //= factor
#         else:
#             factor += 1
#     return max(n, last_factor)

# def main():
#     n = 600851475143
#     print(largest_prime_factor(n))

# if __name__ == "__main__":
#     main()

class PrimeFactorizer:
    def __init__(self, number):
        self.number = number

    def largest_prime_factor(self):
        n = self.number
        factor = 2
        last_factor = 1
        while factor * factor <= n:
            if n % factor == 0:
                last_factor = factor
                n //= factor
            else:
                factor += 1
        return max(n, last_factor)


class PrimeFactorApp:
    def __init__(self):
        self.number = 600851475143

    def run(self):
        factorizer = PrimeFactorizer(self.number)
        result = factorizer.largest_prime_factor()
        print(f"Largest prime factor of {self.number} is {result}")


if __name__ == "__main__":
    app = PrimeFactorApp()
    app.run()
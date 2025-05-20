#####################################################PROBLEM######################################################

# The sum of the squares of the first ten natural numbers is:
# 1² + 2² + ... + 10² = 385

# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)² = 55² = 3025

# Hence, the difference between the sum of the squares of the first ten natural numbers and 
# the square of the sum is:
# 3025 - 385 = 2640

# Now, find the difference between the sum of the squares of the first one hundred natural numbers 
# and the square of the sum.

#################################################SOLUTION#####################################################

# sum_of_squares = 0
# square_of_sum = 0
# for i in range(1, 101):
#     sum_of_squares += i ** 2
#     square_of_sum += i
# square_of_sum = square_of_sum ** 2
# difference = square_of_sum - sum_of_squares
# print(difference)

class SumSquareDifference:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit

    def calculate_sum_of_squares(self):
        sum_of_squares = 0
        for i in range(1, self.upper_limit +1):
            sum_of_squares += i ** 2
            print(i ** 2)
        return sum_of_squares
    
    def calculate_square_of_sum(self):
        square_of_sum = 0
        for i in range(1, self.upper_limit + 1):
            square_of_sum += i
        return square_of_sum ** 2
    
first_one_hundred = SumSquareDifference(100)
print(first_one_hundred.calculate_square_of_sum() - first_one_hundred.calculate_sum_of_squares())
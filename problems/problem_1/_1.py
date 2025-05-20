# #########################################PROBLEM######################################################################
# # If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# # The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

# #########################################SOLUTION######################################################################

# sum = 0
# for number in range(1, 1000):
#     if number % 3 == 0 or number % 5 == 0:
#         sum += number
#         print(number)
# print("The sum of all the multiples of 3 or 5 below 1000 is:", sum)


class MultipleSummer:
    def __init__(self, limit, multiples):
        self.limit = limit
        self.multiples = multiples

    def is_multiple(self, number):
        return any(number % m == 0 for m in self.multiples)

    def calculate_sum(self):
        total = 0
        for number in range(1, self.limit):
            if self.is_multiple(number):
                total += number
        return total


# Usage
summer = MultipleSummer(15, [3, 5])
result = summer.calculate_sum()
print(result)

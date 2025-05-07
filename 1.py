sum = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number
        print(number)
print("The sum of all the multiples of 3 or 5 below 1000 is:", sum)
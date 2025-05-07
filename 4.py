# A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
# Find the largest palindrome made from the product of two $3$-digit numbers

max = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > max:
                max = product
print(max)
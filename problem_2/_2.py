def fibonacci_generator():
    left, right = 0, 1
    while True:
        left, right = right, left + right
        yield left

def sum_even_fibonacci_below(limit):
    total_sum = 0
    for num in fibonacci_generator():
        if num > limit:
            break
        if num % 2 == 0:
            total_sum += num
    return total_sum

def main():
    print(sum_even_fibonacci_below(4_000_000))

if __name__ == "__main__":
    main()
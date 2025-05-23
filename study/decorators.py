def log_args(func):
    def wrapper(*args, **kwargss):
        print(f"Calling function '{func.__name__}' with args=({args}), kwargs={kwargss}")
        result = func(*args, **kwargss)
        print(f"Function '{func.__name__}' returned {result}")
    return wrapper

def log_args_no_return(func):
    print("calling function")
    result = func(1)
    print("result:", result)
    print("function called")

@log_args_no_return
def combine(a, b=2, c=3):
    print("Inside combine function")
    print(f"a={a}, b={b}, c={c}")
    return a + b + c

combine(1, c=20, b=5)
# print(type(test))

# combine(1) = 
# combine(1, b=10)


# WHAT ARE DECORATORS?
# Decorators are a syntactic sugar that are used to pass a function as an argument to another function and modify its behavior.

# WHY DO WE NEED THE WRAPPER FUNCTION?
# Let's analyze the decorator function:
#
# def log_args_no_return(func):
#     print("calling function")
#     result = func(1)
#     print("function called")
#
# @log_args_no_return
# def combine(a, b=2, c=3):
#     print("Inside combine function")
#     print(f"a={a}, b={b}, c={c}")
#     return a + b + c
# combine(1, c=20, b=5)
#
# 1. The interpreter defines the decorator function.

# 2. The decorator operator above the combine function is interpreted as 
#   'combine = log_args_no_return(combine)'.

# 3. So the log_args_no_return function is called with the combine function as an argument,
#    and it prints "calling function", 
#    then calls combine(1) which is the same as combine(1, b=2, c=3), and save the result in the result variable.
#    After that, it prints "function called".
#    Notice that the log_args_no_return function does not return anything, so it returns None by default.

# 4. So the statement of point 2 is equivalent to:
#    combine = None
#
# 5. So when we call combine(1, c=20, b=5) we are actually doing:
#    None(1, c=20, b=5), which result in the error:
#    TypeError: 'NoneType' object is not callable
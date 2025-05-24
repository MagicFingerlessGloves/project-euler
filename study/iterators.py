
# Lists are iterable, meaning you can call iter() on them to get an iterator.
# Then you can use the next() function to get the next item from the iterator.
# So a for loop is just a syntactic sugar for the following code:
nums = [1,2,3]
nums_iter = iter(nums)

while True:
    try:
        num = next(nums_iter)
        print(num)
    except StopIteration:
        break

# We can also create our own iterators by defining a class with __iter__() and __next__() methods.
# It must be an iterable, meaning it must implement the __iter__() method that returns an iterator.
# Since the Class is supposed to be an iterator, it must also implement the __next__() method
# meaning that the __iter__() method can (and should) return self.

class MyRange:    
    """A simple iterator that mimics the behavior of range(start, end)"""

    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            value = self.current
            self.current += 1
            return value
        
nums = MyRange(1, 5)
for num in nums:
    print(num)

# Notice that the syntax might be a bit confusing, so here come generators.
# The yield keyword allows us to create a generator function, which is a simpler way to create an iterator.
def my_range(start, end):
    """A simple generator that mimics the behavior of range(start, end)"""
    current = start
    while current < end:
        yield current 
        current += 1
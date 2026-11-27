from functools import reduce

# Create a list
numbers = [1, 2, 3, 4, 5, 6]

# Using map() to find squares
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# Using filter() to find even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Using reduce() to find the sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", total)
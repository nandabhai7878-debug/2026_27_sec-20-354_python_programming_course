# Define a function
def divide(a, b):
    return a / b

# Call using keyword arguments
result1 = divide(b=10, a=20)
print("Result using keyword arguments:", result1)

# Call using positional arguments
result2 = divide(10, 20)
print("Result using positional arguments:", result2)
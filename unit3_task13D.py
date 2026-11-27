# Recursive function to generate Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get input from the user
n = int(input("Enter the number of terms: "))

# Generate Fibonacci series
print("Fibonacci series:")
for i in range(n):
    print(fibonacci(i), end=" ")
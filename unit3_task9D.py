# Global variable
x = 100

# Function with a local variable
def display():
    x = 50
    print("Local variable x:", x)

# Display global variable
print("Global variable before function call:", x)

# Call the function
display()

# Display global variable again
print("Global variable after function call:", x)
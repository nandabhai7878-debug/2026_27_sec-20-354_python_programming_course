# Global counter
counter = 0

# Function to increment counter
def increment():
    global counter
    counter += 1
    print("Counter:", counter)

# Call the function multiple times
increment()
increment()
increment()
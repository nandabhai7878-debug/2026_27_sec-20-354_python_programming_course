# Function to calculate area and perimeter
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Get input from the user
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

# Call the function
area, perimeter = rectangle(length, breadth)

# Display the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)
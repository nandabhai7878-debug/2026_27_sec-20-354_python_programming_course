# Create two matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Matrix Addition
print("Matrix Addition:")
for i in range(2):
    for j in range(2):
        print(A[i][j] + B[i][j], end=" ")
    print()

# Matrix Subtraction
print("\nMatrix Subtraction:")
for i in range(2):
    for j in range(2):
        print(A[i][j] - B[i][j], end=" ")
    print()

# Matrix Multiplication
print("\nMatrix Multiplication:")
for i in range(2):
    for j in range(2):
        result = 0
        for k in range(2):
            result += A[i][k] * B[k][j]
        print(result, end=" ")
    print()

# Matrix Transpose
print("\nTranspose of Matrix A:")
for i in range(2):
    for j in range(2):
        print(A[j][i], end=" ")
    print()
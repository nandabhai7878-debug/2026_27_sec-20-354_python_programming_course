
n = int(input("Enter a number (1-100): "))
count = 0

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            count += 1
            break

    if count == 0:
        print("Prime number")
    else:
        print("Not a prime number")
else:
    print("Not a prime number")

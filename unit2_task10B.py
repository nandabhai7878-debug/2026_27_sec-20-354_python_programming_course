n = int(input("Enter a number: "))
num = abs(n)
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if n < 0:
    reverse = -reverse

print("Reversed number:", reverse)
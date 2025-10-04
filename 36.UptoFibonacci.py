limit = int(input("Enter the limit: "))

a, b = 0, 1  # First two Fibonacci numbers
print("Fibonacci numbers up to", limit, ":")

while a <= limit:
    print(a, end=" ")
    a, b = b, a + b

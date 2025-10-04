def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(limit):
    a, b = 0, 1
    fib_numbers = []
    while a <= limit:
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers

# Example usage
limit = int(input("Enter the limit: "))
fib_numbers = fibonacci(limit)

print("Fibonacci numbers that are prime:")
for num in fib_numbers:
    if is_prime(num):
        print(num, end=" ")

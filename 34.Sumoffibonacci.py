def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("Enter a number: "))
fib_sum = 0
for i in range(num):
    fib_sum += fibonacci(i)
print(f"Sum of first {num} fibonacci numbers is {fib_sum}")
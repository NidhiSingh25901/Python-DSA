# Dictionary to store computed Fibonacci numbers
memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    
    memo[n] = result  # Store the result in dictionary
    return result

# Example usage: generate first n Fibonacci numbers
n = int(input("Enter the number of terms: "))
print("Fibonacci sequence with memoization:")
for i in range(n):
    print(fibonacci(i), end=" ")

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def fibonacci_palindromes(n_count):
    fib1, fib2 = 0, 1
    count = 0
    result = []
    
    while count < n_count:
        if is_palindrome(fib1):
            result.append(fib1)
            count += 1
        fib1, fib2 = fib2, fib1 + fib2
    
    return result

# Example usage
N = int(input("Enter N: "))
palin_fibs = fibonacci_palindromes(N)
print(f"The first {N} Fibonacci numbers that are palindromes are:")
print(palin_fibs)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:  # check 6k-1 and 6k+1
            return False
        i += 6
    return True

# Test
for num in [2, 3, 4, 5, 11, 25, 31]:
    print(num, is_prime(num))

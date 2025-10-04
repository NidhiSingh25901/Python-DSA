def trailing_zeros(x):
    count = 0
    while x >= 5:
        x //= 5
        count += x
    return count

def smallest_number_with_n_zeros(N):
    low, high = 0, 5 * N  # Upper bound: 5*N is safe
    answer = -1
    
    while low <= high:
        mid = (low + high) // 2
        if trailing_zeros(mid) >= N:
            answer = mid
            high = mid - 1  # Look for smaller number
        else:
            low = mid + 1
            
    return answer

# Example usage
N = int(input("Enter number of trailing zeros: "))
result = smallest_number_with_n_zeros(N)
print(f"The smallest number whose factorial has at least {N} trailing zeros is {result}")

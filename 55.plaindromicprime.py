def if_palindromic(num):
    return str(num) == str(num)[::-1] 

def if_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True 

num = input("Enter a number:")

int_num = int(num) 

if if_palindromic(num) and if_prime(int_num):
    print(num, "is a palindromic prime")
else:
    print(num, "is not a palindromic prime")
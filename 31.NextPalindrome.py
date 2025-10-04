def is_palindrome(n):
    return str(n) == str(n)[::-1]  # Convert number to string and check reverse

num = int(input("Enter a number: "))

next_num = num + 1
while True:
    if is_palindrome(next_num):
        print(f"The next palindrome after {num} is {next_num}")
        break
    next_num += 1

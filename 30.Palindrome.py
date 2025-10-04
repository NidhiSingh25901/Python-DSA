num = int(input("Enter a number:")) 

original = num
reverse = 0
temp = num

while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == original:
    print(f"{num} is a palindrome") 
else:
    print(f"{num} is not a palindrome")

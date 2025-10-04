name = input("Enter sentence:") 
name = name.replace(" ", "").lower()
if(name==name[::-1]):
    print(f"{name} is a palindrome")
else:
    print(f"{name} is not a palindrome")
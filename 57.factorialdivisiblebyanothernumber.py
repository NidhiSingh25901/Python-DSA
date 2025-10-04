num= int(input("Enter a number: ")) 
num2 = int(input("Enter another number: "))
factorial =1

for i in range(1,num+1):
    factorial *= i 

if(factorial % num2==0):
    print(f"{num2} is divisible by {num}!")

else:
    print(f"{num2} is not divisible by {num}!")
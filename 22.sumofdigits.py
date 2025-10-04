num = int(input("Enter a number:")) 

temp=num
sum =0 

while(temp!=0):
    digit = temp%10
    sum+=digit
    temp = temp//10

print(f"Sum of digits is {sum}")

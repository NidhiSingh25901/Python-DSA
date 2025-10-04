num = int(input("Enter a number:")) 
temp = num 

#Approach 1
while(temp !=0):  
    digit = temp % 10
    print(digit, end="")
    temp = temp // 10

#Approach 2
reverse=0
while(temp !=0):  
    digit = temp % 10
    reverse= reverse*10 + digit
    temp = temp // 10

print(f"Reverse of {num} is {reverse}")

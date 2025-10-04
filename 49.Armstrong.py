num = int(input("Enter a number:")) 

string = str(num)
length = len(string) 

temp =num
sum=0
r=0
while(temp!=0):
    r = temp % 10
    sum = sum + (r ** length)
    temp = temp // 10 

if(sum==num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
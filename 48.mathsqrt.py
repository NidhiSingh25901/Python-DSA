import math

num = int(input("Enter a number:")) 

root = int(math.sqrt(num)) 

if(root*root ==num):
    print(f"{num} is a perfect square") 
else:
    print(f"{num} is not a perfect square")
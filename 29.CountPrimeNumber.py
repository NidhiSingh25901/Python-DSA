def is_prime(num):
    c=0

    for i in range(2,num):
        if(num%i==0):
            c+=1        
    if(c==0 and num!=1):
        return True
    
num = int(input('Enter a number:')) 
count=0
for j in range(1,num+1):
    if is_prime(j):
        count+=1
print(f"Count of prime number between 1 to {num} is {count}")
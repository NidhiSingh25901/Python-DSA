def isprime(num):
    if(num<2):
        return False 
    for i in range(2, int(num**0.5)+1):
        if(num%i==0):
            return False
    return True

n = int(input('Enter a number:')) 
count =0
num =2

while True:
    if isprime(num):
        count +=1
        if count == n:
            print(f"{n}th prime number is {num}")
            break
    num +=1
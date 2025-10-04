firstnum = int(input("Enter first number:")) 
secondnum = int(input("Enter second number:"))
thirdnum = int(input("Enter third number:")) 

if(firstnum >= secondnum) and (firstnum >= thirdnum):
    largest = firstnum
elif(secondnum >= firstnum) and (secondnum >= thirdnum):
    largest = secondnum
else:
    largest = thirdnum 

print("The largest number is", largest)
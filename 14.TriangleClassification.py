firstlength = int(input("Enter length of first side:"))
secondlength = int(input("Enter length of second side:"))
thirdlength = int(input("Enter length of third side:"))

if(firstlength == secondlength == thirdlength):
    print("The triangle is equilateral")
elif(firstlength == secondlength or secondlength == thirdlength or firstlength == thirdlength):
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")
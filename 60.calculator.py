firstnum = int(input("Enter first number:")) 
secondnum = int(input("Enter second number:")) 

operation = input("Enter operation (+, -, *, /): ") 

if operation == '+':
    result = firstnum + secondnum
    print(f"The sum of {firstnum} and {secondnum} is {result}")
elif operation == '-':
    result = firstnum - secondnum
    print(f"The difference between {firstnum} and {secondnum} is {result}")
elif operation == '*':
    result = firstnum * secondnum
    print(f"The product of {firstnum} and {secondnum} is {result}")
elif operation == '/':
    if secondnum != 0:
        result = firstnum / secondnum
        print(f"The division of {firstnum} by {secondnum} gives {result}")
    else:
        print("Error: Division by zero is not allowed.")
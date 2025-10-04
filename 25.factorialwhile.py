num = int(input("Enter a number: ")) 

factorial = 1
i = 1

while i <= num:        # Correct condition using 'i'
    factorial *= i
    i += 1

print(f"Factorial of {num} is {factorial}")

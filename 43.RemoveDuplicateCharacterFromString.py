var = input("Enter a string:") 

new_var = "" 

freq={}

for i in var:
    if i not in new_var:
        new_var=new_var+i

print("String after removing duplicate characters:", new_var)
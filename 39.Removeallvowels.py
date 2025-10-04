name = input("Enter a string:") 

for i in name:
    if i in 'aeiouAEIOU':
        name = name.replace(i, "") 
print("String after removing vowels:", name)
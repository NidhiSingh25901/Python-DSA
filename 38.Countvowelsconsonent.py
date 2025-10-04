name = input("Enter a string:") 

cleane_name = name.replace(" ", "").lower() 

for i in range(len(cleane_name)): 
    if cleane_name[i] in 'aeiou': 
        print(f"{cleane_name[i]} is a vowel") 
    else: 
        print(f"{cleane_name[i]} is a consonant")
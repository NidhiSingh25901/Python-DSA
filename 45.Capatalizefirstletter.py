import string
var = input("Enter a string:") 

sentence_clean = var.translate(str.maketrans('', '', string.punctuation))
words = sentence_clean.split()
new_var = ""
for word in words:
    new_var += word.capitalize() + " "
print("String after capitalizing first letter of each word:", new_var.strip())


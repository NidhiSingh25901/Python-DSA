var1 = input("Enter first string: ")
var2 = input("Enter second string: ")

if sorted(var1) == sorted(var2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
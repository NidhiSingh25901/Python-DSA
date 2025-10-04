#Approach 1: Using a dictionary to count frequencies
string = input("Enter a string: ")
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")


#Approach 2: Using collections.Counter
from collections import Counter

string = input("Enter a string: ")
freq = Counter(string)

print("Character frequencies:")
for char, count in freq.items():
    print(f"'{char}': {count}")


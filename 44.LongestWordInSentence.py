import string

sentence = input("Enter a sentence: ")

# Remove punctuation
sentence_clean = sentence.translate(str.maketrans('', '', string.punctuation))

words = sentence_clean.split()
longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print(f"The longest word is '{longest_word}' with length {max_length}.")

sentence = "Madam Arora teaches malayalam"

# Split the sentence into words
words = sentence.split()

# Initialize a counter for palindrome words
palindrome_count = 0

# Iterate over each word and check if it's a palindrome
for word in words:
    # Remove any punctuation and convert to lowercase for accurate comparison
    cleaned_word = ''.join(filter(str.isalnum, word)).lower()
    if cleaned_word == cleaned_word[::-1]:
        palindrome_count += 1

print(f"Number of palindrome words: {palindrome_count}")

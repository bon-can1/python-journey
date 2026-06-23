# Use built-in string functions.
# Strings have many useful methods — they help you clean, check, and change text.
# Most string methods return a NEW string (strings do not change in place).

text = "  Hello Python World  "

# case methods
print(text.upper())          # HELLO PYTHON WORLD
print(text.lower())          # hello python world
print(text.title())          # Hello Python World
print(text.capitalize())     # first letter only

# strip removes spaces from start and end
print(text.strip())          # Hello Python World

# find and count
sentence = "python is fun and python is powerful"
print(sentence.find("python"))     # 0 (first match index)
print(sentence.rfind("python"))    # 19 (last match index)
print(sentence.count("python"))    # 2

# check content
email = "user@gmail.com"
print(email.startswith("user"))    # True
print(email.endswith(".com"))      # True
print("123".isdigit())             # True
print("Hello".isalpha())           # True
print("Hello123".isalnum())        # True

# split into words
words = sentence.split()
print(words)

############################################################

# Word Counter
# Count how many words the user typed.

sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")
print("Words:", words)

############################################################

# Palindrome Checker
# Check if a word reads the same forward and backward (ignore case and spaces).

word = input("Enter a word: ")
clean = word.lower().replace(" ", "")

if clean == clean[::-1]:
    print(f'"{word}" is a palindrome!')
else:
    print(f'"{word}" is NOT a palindrome.')

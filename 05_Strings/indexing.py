# Access individual characters.
# Strings are sequences — each character has a position called an index.
# Indexing starts at 0 for the first character.
# You can also use negative indexes: -1 is the last character, -2 is second last, etc.
# If you use an index that does not exist, Python raises IndexError.

text = "Python"

# positive indexing (left to right)   print's
print("First character:", text[0])    # P
print("Third character:", text[2])    # t
print("Last character:", text[5])     # n

# negative indexing (right to left)
print("Last character:", text[-1])    # n
print("Second last:", text[-2])       # o
print("First character:", text[-6])   # P

# indexing with a variable
index = 1
print(f"Character at index {index}:", text[index])

# strings are immutable — you cannot change a character directly
# text[0] = "J"  # TypeError

# loop through characters using indexing
word = "code"
for i in range(len(word)):
    print(f"Index {i}: {word[i]}")

############################################################

# First and Last Letter Checker
# Ask the user for a word and print its first and last letters.

word = input("Enter a word: ")

if len(word) == 0:
    print("You entered an empty word.")
else:
    print(f"First letter: {word[0]}")
    print(f"Last letter: {word[-1]}")

############################################################

# Reverse a Word Using Indexing
# Build the reversed word by reading characters from the end.

word = input("Enter a word to reverse: ")
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("Original:", word)
print("Reversed:", reversed_word)


###### process
# len(word) gives total number of characters
# Example:
# word = "hello"
# len(word) = 5

# String indexing:
# h e l l o
# 0 1 2 3 4

# range(len(word)-1, -1, -1)
# becomes:
# range(4, -1, -1)

# Start = 4 (last index)
# Stop = -1 (not included)
# Step = -1 (move backwards)

# Loop sequence:
# i = 4 -> word[4] = o
# i = 3 -> word[3] = l
# i = 2 -> word[2] = l
# i = 1 -> word[1] = e
# i = 0 -> word[0] = h

# reversed_word += word[i]
# Adds each character to the new string

# Iteration Process:
# ""      + "o" = "o"
# "o"     + "l" = "ol"
# "ol"    + "l" = "oll"
# "oll"   + "e" = "olle"
# "olle"  + "h" = "olleh"

# Final Output:
# Original : hello
# Reversed : olleh

###################################################################################
# Combine list items into strings.
# join() is the opposite of split().
# You call join on a separator string: separator.join(list)
# Every item in the list must be a string.

words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)

# different separators
numbers = ["1", "2", "3", "4", "5"]
print("-".join(numbers))       # 1-2-3-4-5
print(", ".join(numbers))      # 1, 2, 3, 4, 5
print("".join(numbers))        # 12345

# join after split (reverse operation)
text = "apple-banana-mango"
fruits = text.split("-")
back_to_text = " | ".join(fruits)
print(back_to_text)

# join with newline for multi-line text
lines = ["Welcome to Python", "Start learning today", "Good luck!"]
paragraph = "\n".join(lines)
print(paragraph)

# convert numbers to strings before joining
scores = [85, 90, 78]
score_text = ", ".join(str(score) for score in scores)
print("Scores:", score_text)

############################################################

# Acronym Maker
# Take a phrase and join the first letter of each word.

phrase = input("Enter a phrase: ")
words = phrase.split()
acronym = "".join(word[0].upper() for word in words)
print("Acronym:", acronym)

############################################################

# Password Generator from Words
# Combine 3 random words with a separator to make a password.

word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")
word3 = input("Enter word 3: ")

password = "-".join([word1, word2, word3])
print("Your password:", password)

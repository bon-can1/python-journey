# Replace text within strings.
# replace(old, new) swaps old text with new text.
# replace(old, new, count) replaces only the first 'count' matches.
# The original string stays the same — replace() returns a new string.

text = "I love Java. Java is good. I want to learn Java."

# replace all matches
new_text = text.replace("Java", "Python")
print(new_text)

# replace only first 2 matches
partial = text.replace("Java", "Python", 2)
print(partial)

# remove characters by replacing with empty string
message = "Hello!!!"
clean = message.replace("!", "")
print(clean)

# replace spaces
data = "apple, banana, mango"
fixed = data.replace(", ", " | ")
print(fixed)

# case-sensitive — "java" and "Java" are different
word = "Python python PYTHON"
print(word.replace("python", "code"))       # only lowercase match
print(word.replace("Python", "code"))       # only first match

############################################################

# Censor Bad Words
# Replace bad words in a sentence with ****.

sentence = input("Enter a sentence: ")
bad_words = ["bad", "hate", "stupid"]

for word in bad_words:
    sentence = sentence.replace(word, "****")

print("Clean sentence:", sentence)

############################################################

# Phone Number Formatter
# Replace dashes and spaces, then format as XXX-XXX-XXXX.

number = input("Enter phone number (any format): ")
number = number.replace("-", "").replace(" ", "")

if len(number) == 10 and number.isdigit():
    formatted = number[:3] + "-" + number[3:6] + "-" + number[6:]
    print("Formatted number:", formatted)
else:
    print("Invalid number. Enter 10 digits.")

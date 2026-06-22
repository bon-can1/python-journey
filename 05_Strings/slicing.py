# Extract portions of strings.
# Slicing lets you get a part of a string using [start:stop:step].
# start — where to begin (included)
# stop  — where to end (NOT included)
# step  — how many characters to jump (default is 1)

text = "Python Journey"

# basic slicing
print(text[0:6])      # Python
print(text[7:14])     # Journey
print(text[:6])       # Python (from start)
print(text[7:])       # Journey (till end)

# negative indexes in slicing
print(text[-7:])      # Journey
print(text[0:-8])     # Python

# step slicing
print(text[::2])      # PtoJuny (every 2nd character)
print(text[::-1])     # reverse the whole string

# useful tricks
word = "Hello"
print(word[1:4])      # ell
print(word[:3])       # Hel
print(word[2:])       # llo

############################################################

# Username Generator
# Take a full name and create a username from first 3 letters + last 2 letters.

full_name = input("Enter your full name: ").replace(" ", "").lower()

if len(full_name) < 5:
    print("Name is too short. Use at least 5 letters.")
else:
    username = full_name[:3] + full_name[-2:]
    print(f"Generated username: {username}")

############################################################

# Hide Middle of a Word
# Show first 2 and last 2 characters, hide the middle with stars.

word = input("Enter a word: ")

if len(word) <= 4:
    print("Word must be longer than 4 characters.")
else:
    hidden = word[:2] + "*" * (len(word) - 4) + word[-2:]
    print("Hidden word:", hidden)

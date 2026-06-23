# Split strings into lists.
# split() breaks a string into a list of smaller strings.
# By default it splits on spaces.
# You can split on any character or word using split(separator).

text = "apple banana mango grape"
fruits = text.split()
print(fruits)

# split on a specific character
data = "name=Arun,age=20,city=Wayanad"
pairs = data.split(",")
print(pairs)

# split with max splits
sentence = "one-two-three-four-five"
parts = sentence.split("-", 2)   # split only 2 times
print(parts)

# split lines
paragraph = "Line 1\nLine 2\nLine 3"
lines = paragraph.split("\n")
print(lines)

# split and unpack
full_name = "Arun Boban"
first, last = full_name.split()
print("First:", first)
print("Last:", last)

# empty string after split
csv = "10,20,30,"
numbers = csv.split(",")
print(numbers)

############################################################

# CSV Name Splitter
# Split a comma-separated list and print each item numbered.

items = input("Enter items separated by commas: ")
item_list = items.split(",")

print("\nYour list:")
for i, item in enumerate(item_list, start=1):
    print(f"{i}. {item.strip()}")

############################################################

# Email Username Extractor
# Split email at @ and show the username part.

email = input("Enter your email: ")

if "@" in email:
    username, domain = email.split("@")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email format.")

# Extract tuple sections.
# Slicing is used to access multiple elements from a tuple
# It extracts a portion of a tuple
# Slicing creates a NEW tuple
# The original tuple remains unchanged
# Slicing uses start, stop, and step values
# The stop index is NOT included
# Tuple slicing works the same way as list slicing


# example 1  basic slicing
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])


# example 2  negative slicing
print(numbers[-3:])
print(numbers[:-2])


# example 3  step slicing
print(numbers[::2])
print(numbers[::-1])


# example 4  string tuple slicing
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print(days[0:5])
print(days[5:])


# example 5  slicing nested tuple
data = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(data[1])
print(data[1][0:2])


# ==========================================================
# MINI PROJECT 1
# WEEKEND EXTRACTOR
# ==========================================================

# Extract only the weekend days from a full week tuple.

week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

weekend = week[5:]

print("Full Week:", week)
print("Weekend:", weekend)


# ==========================================================
# MINI PROJECT 2
# SCORE SUMMARY
# ==========================================================

# Take 5 test scores and show the highest 3 scores using slicing.

score1 = int(input("Enter score 1: "))
score2 = int(input("Enter score 2: "))
score3 = int(input("Enter score 3: "))
score4 = int(input("Enter score 4: "))
score5 = int(input("Enter score 5: "))

scores = (score1, score2, score3, score4, score5)
sorted_scores = tuple(sorted(scores, reverse=True))
top_three = sorted_scores[:3]

print("\nAll Scores:", scores)
print("Top 3 Scores:", top_three)

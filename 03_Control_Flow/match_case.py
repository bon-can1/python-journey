# Modern alternative to multiple if statements.
# match-case works like switch in other languages (Python 3.10+)

command = "start"

match command:
    case "start":
        print("Starting the program...")
    case "stop":
        print("Stopping the program...")
    case "pause":
        print("Pausing the program...")
    case _:
        print("Unknown command.")

# matching numbers
day = 5

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:
        print("Weekend!")
    case _:
        print("Invalid day")

# matching with conditions (guard)
score = 92

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 80:
        print("Grade: B")
    case s if s >= 70:
        print("Grade: C")
    case s if s >= 50:
        print("Grade: D")
    case _:
        print("Grade: F")

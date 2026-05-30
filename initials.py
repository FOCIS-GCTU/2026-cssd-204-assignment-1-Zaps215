# File: initials.py
# Description: Print out my initials E, A, A in stylized large letters
# Assignment Number: 1
#
# Name: Emmanuel Akolbilla Alhassan Ananga
# STUDENT ID: 2425402086
# Email: 2425402086@live.gctu.edu.gh
# Grader: Mr. Augustus Buckman
#
# On my honor, Emmanuel Akolbilla Alhassan Ananga, this programming assignment is my own work
# and I have not provided this code to any other student.

# Letter E - 10 rows, 12 chars wide
e0 = "EEEEEEEEEEEE"
e1 = "EEE........."
e2 = "EEE........."
e3 = "EEE........."
e4 = "EEEEEEEEEEEE"
e5 = "EEEEEEEEEEEE"
e6 = "EEE........."
e7 = "EEE........."
e8 = "EEE........."
e9 = "EEEEEEEEEEEE"

# Letter A - 10 rows, 12 chars wide
a0 =  "....AAAA...."
a1 =  "...AA..AA..."
a2 =  "..AA....AA.."
a3 =  ".AA......AA."
a4 =  "AA........AA"
a5 =  "AAAAAAAAAAAA"
a6 =  "AA........AA"
a7 =  "AA........AA"
a8 =  "AA........AA"
a9 =  "AA........AA"


def main():
    # Print small initials line with periods
    print()
    print("...EAA")
    print()

    # Print large initials - 10 rows high
    # Each row: 3 periods(...) before and after the letter and a 4 (*) asteriks after to serve as a space between the other letters
    print("..." + e0 + "........" + a0 + "........" + a0 + ".....")
    print("..." + e1 + "........" + a1 + "........" + a1 + ".....")
    print("..." + e2 + "........" + a2 + "........" + a2 + ".....")
    print("..." + e3 + "........" + a3 + "........" + a3 + ".....")
    print("..." + e4 + "........" + a4 + "........" + a4 + ".....")
    print("..." + e5 + "........" + a5 + "........" + a5 + ".....")
    print("..." + e6 + "........" + a6 + "........" + a6 + ".....")
    print("..." + e7 + "........" + a7 + "........" + a7 + ".....")
    print("..." + e8 + "...**..." + a8 + "...**..." + a8 + "...**")
    print("..." + e9 + "...**..." + a9 + "...**..." + a9 + "...**")

    # Final blank line
    print()


# Call the main function
if __name__ == "__main__":
    main()


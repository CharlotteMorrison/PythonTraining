#Write a program that displays the letter grade for a test gie the score out of 100
#(90-100 A, 80-89 B, 70-79 C, else FAIL)

grade = int(raw_input("Enter your grade: "))

if (grade >= 90):
    print("Your grade is an A!")
elif (grade >= 80):
    print("Your grade is a B!")
elif (grade >=70):
    print("Your grade is a C.")
else:
    print("FAIL")

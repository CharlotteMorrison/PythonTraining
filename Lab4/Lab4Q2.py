#Write a program that prints the first few verses of the travelling song
#"100 bottles of beer". Use a loop such that each iteration prints one verse.
#Read the number of verses to print from the user.
#Validate the input.

number = int(raw_input("How many verses should I sing? Enter a number between 1-100"))

#validate input
while (number < 0 and number > 100):
    number = int(raw_input("That was not a valid input? Enter a number between 1-100"))


for i in range(number, -1, -1):
    print(str(i) + " bugs in the code.")
    print(str(i) + " bugs in the code.")
    print("Pull one down, a patch is found.")
    print(str(i - 1) + "bugs in the code.")
    print(" ")
    if (i == 1):
        print(" ")
        print(str(number + 99) + " BUGS IN THE CODE!")
        break
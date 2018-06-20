#Write a program that asks the user to guess a computer generated number.
#The user gets 3 chances and the program provides feedback if the number is
#higher or lower than the number guessed.

import random

#generates a random number between 1 and 10
number = random.randint(1,10)

#instantiates guess at a number that is not correct to start while loop
#instantiates counter
guess, count = 0

while (guess != number and count < 3):
    guess = int(raw_input("Guess a number between 1 and 10"))
    if (guess == number):
        print("YOU WIN!!!!!")
    elif (guess >= number):
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    count+=1
#Write a program that allows the user to input 3 bowling scores between
#0 and 300.  The program must display the average of the scores.

score1 = int(raw_input("Please enter score 1: "))
score2 = int(raw_input("Please enter score 2: "))
score3 = int(raw_input("Please enter score 3: "))

average = (score1 + score2 + score3)/3

print("Your average score is: " + str(average))
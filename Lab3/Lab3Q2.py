#Write a program that takes in a password as a string and checks to see
#if the length of the password is the right size (7 to 8 charactors)

password = raw_input("Enter your password: ")

if (len(password) >= 7):
    if (len(password)<= 8):
        print("Your password is the right length.")
    else:
        print("Your password is longer than 8 characters.")
else:
    print("Your password is too short.")
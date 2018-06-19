#Write a program that asks the user for the lengthe and width of a rectangular
#wooden plank and calculates the area and perimeter

#get input (raw_input is Python 2, use just input in python 3
length = int(raw_input("Please enter the length: "))
width = int(raw_input("Please enter the width: "))


#compute area and perimeter
area = length * width
perimeter =  2 * length + 2 * width

#print values (must cast int to string to concatenate the response)
print("The area is: " + str(area))
print("The perimeter is: " + str(perimeter))
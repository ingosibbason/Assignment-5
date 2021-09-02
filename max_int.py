#Get int inputs from user until input is negative
#Find the highest input and print it

max_int = 0
num_int = 0

while num_int > -1:
    num_int = int(input("Input a number: "))    # Do not change this line

    if num_int > max_int:
        max_int = num_int



print("The maximum is", max_int)    # Do not change this line

#program for guessing the number . in order to write the program we have to use the one of the python function that will genrate the number for the given range of the function.
# first of all we have to import some libraries for the generting the random number which is shown below
import random
#next we have to use the random function  for the given range of the value for example we have here taken the values 1-11 . it will automatically generates the single valye.
Random=random.randrange(1,11)
#then enter a value that can store in the NUmber variable and that number will the user guessing number
a= input("Enter the user Guessing number in the range between 1 to 11:")
Number= int(a)


# now we have to write the coondition if we guess a number that would be the user guessing number.
if(Number>Random):
#now we have to print the given condition
    print("Your Entered  Guessing Number is higher than Required")
#now we have to use else if what we use in python was elif as the condition
elif Number<Random:
# now we have to print the given condition
    print("Your Entered Guessing Number is lower than required")

else:
# now we have to print the given condition
    print("Your answer is PERFECT GUESS!! Congratulations!!")


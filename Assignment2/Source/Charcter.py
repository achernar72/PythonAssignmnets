#importing some libraries required for the program string and sys libraries
import string, sys
#this is th function where the given input and alphabert set will be compared

def ispangram(str1, alphabet=string.ascii_lowercase):

#we are taking the alpha value as the all alphabet set
    alpha = set(alphabet)
# now ewe are returining the alphabet values in lowercase form

    return alpha <= set(str1.lower())


#this print  and function statement will check the alphabets was the input string the result will be displaed as true or false
print(ispangram(input("enter the string you want to check:")))

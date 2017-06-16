# Write the program for EvenOrOdd condition in this program user gives a input the out put will tells that user INput is even or Odd
# the user input has to be stored in the variable "a"
a= input("Enter the number:")
#The number entered is stored in the Number value
Number= int(a)


#Condition for this program is that we know that if any number divisible  by 2  will gets the reminder then it will be the even number
# or  in any condition it wil be considered it as the  odd number.

if(Number%2==0):

#now we are printing the result by using the print function if it is equals to zero then it is prints even
    print("The Entered Number",Number,"is Even")
else:

#now we are printing the result by using the print function if it is not equals to zero then it prints odd

    print("The Entered NUmber",Number,"is Odd")



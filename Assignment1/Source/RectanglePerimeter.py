#Program for the python, given conditions are Take length and breadth from a user for a rectangle and calculate perimeter for the same.
# storing the values of the length and breadth values in the l and b letters and they will store in them.taken from the console and stored.


l=input("Enter the value of the length :")
b=input("Enter the value of the breadth :")


# Assigning the variable types to length and breadth

length= int(l)
breadth= int(b)



#Formula for the permeter of the rectangle , which is length+length+breadth+breadth=2(length+breadth)

perimeter= 2*(length+breadth)

#printing the values of the perimeter10

print("perimeter of a rectangle is :",perimeter)
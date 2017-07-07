#IN order to write a program for the dictionaries to perform some operations we have to create dictionary set
# we called the set name as student info
stud_info= [
  {'name' : 'raju', 'branch' : 'computer science', 'old scores' : 90, 'recent scores' : 70},
  {'name' : 'vasu', 'branch' : 'electrical engineering', 'old scores' : 99, 'recent scores' : 84},
  {'name' : 'siva', 'branch' : 'computer science', 'old scores' : 80, 'recent scores' : 99}
]
#it will print the stud_ info
print(stud_info)
print("")
print("   you can observe the changes   ")
print("")
# then we have to write the function use the for loop to select the required column by choosing the names old scores and new scores . we have to find the average for those.
def average(dictionary):
    for d in dictionary:
        c2 = d.pop('old scores')
        c3 = d.pop('recent scores')
        d['old scores + recent scores'] = (c2 + c3)/2
        #we have to return the average value and display in the stud_info
    return dictionary
# which will print the student info
print(average(stud_info))
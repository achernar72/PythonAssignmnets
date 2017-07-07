#program for the symmetry and we have to remove the same values
#so for that we have to consider two sets where we use the ^ function and remove the similar pairs from different intersection
#iN ONE OF THE SET I HAVE TAKEN CAR COMPANIES
a = set(["Toyota", "Benz","Audi","Jeep"])
#IN ONE OF THE SET B I HAVVE TAKEN CAR BRANDS AND USED STORED IN SET B
b = set(["Benz", "GMC"])
#i  N ORDER TO REMOVE THE SAME VALUES IN DIFFERENT SETS WE USE THE BELOW FUNCTION WHERE IT CAN VOID THE SAME VALUES TO ZERO
RESULT = a ^ b
#NOW WE ARE GOING TO DISPLAY THE RESULT
print(RESULT)
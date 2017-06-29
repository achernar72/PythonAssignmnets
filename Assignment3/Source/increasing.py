#given the numbers in the list  and it stired in the list name things
l=[(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]
#i  order to sort he given terms and lambda value where it selects the second position i n the tuple and soreted as in the increasing order.
op = sorted(l, key=lambda x: x[-1])
#print the output
print (op)

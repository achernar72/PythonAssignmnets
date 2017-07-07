#in order to write a program for the sorted sequence seperated b a comma we have to take input from the user so we have to use first the input function which it can take the input from the user
sentence = input("Enter the words in sequence seperated by the comma:")
# now we have to take the seperated word as the word so we divide the sentence by identifyig the comma after each word
sortedword = [word for word in sentence.split(",")]
#now we have to sort the words by using the sort function and it will display i n alphabetical order
#now we are printing the result using the print function
print(",".join(sorted(list(set(sortedword)))))
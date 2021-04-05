# A program that reads in a text file and outputs the number of e's it contains.
# Author: Mantvydas Jokubaitis

# Importing sys so file can be read from the comand line 
import sys
countedletter = "e"

with open(sys.argv[1], 'r') as f:
    data = f.read()
    data = data.casefold() #Letter to lower case
    lettercount = data.count(countedletter) #Letters counted
print("You have {} of letters '{}' in this text. " .format(lettercount, countedletter))



# Letters an be also counted using function method below, it is case sensitive though:
'''
import sys
countedletter = "E"
count=0

with open(sys.argv[1], 'r') as f:
    for line in f:
        for letter in line:
            if(letter==countedletter):
                count +=1
print("You have {} of letters '{}' in this text. " .format(count, countedletter))
'''
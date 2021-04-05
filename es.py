# A program that reads in a text file and outputs the number of e's it contains.
# Author: Mantvydas Jokubaitis

with open("mobydick.txt", 'r') as f:
    data = f.read()
    count = data.casefold()
    count = count.strip()
    lettercount = count.count('e')
print("Number of e's in the text: " +count )

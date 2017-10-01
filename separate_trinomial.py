#separate_trinomial.py
#takes in a text file with trinomials, splits it with the trinomial split function, and spits it out 
#as a CSV file.

import sys #for command line args.
import trinomialsplit as ts

#grab command line arg
filename = sys.argv[1]

#open and read the file
file_object = open(filename, 'r')

with file_object as f:
    trinom_list = file_object.readlines()

trinom_list = [i.strip() for i in trinom_list]

stateList = []

for i in range(0, len(trinom_list) - 1):
    # grap all of the characters per line that are basically not whitespace.
    tempstr = ""
    for j in range(0, len(trinom_list[i])):
        if trinom_list[i][j].isalpha() or trinom_list[i][j].isdigit():
            tempstr += trinom_list[i][j]
    
    tempts = ts.TrinomialSplit(tempstr)
    #print(trinom_list[i])
    stateList.append(tempts.get_state_code)

print(stateList)






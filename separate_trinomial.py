#separate_trinomial.py
#takes in a text file with trinomials, splits it with the trinomial split function, and spits it out 
#as a CSV file.

import sys #for command line args.
import trinomialsplit as ts
import csv

#grab command line arg
filename = sys.argv[1]

#open and read the file in as a list object.
file_object = open(filename, 'r')

with file_object as f:
    trinom_list = file_object.readlines()

#strip out pesky new lines
trinom_list = [i.strip() for i in trinom_list]

# These lists are where state numbers, county codes, and site numbers are stored.
stateList = []
countylist = []
sitelist = []

for i in range(0, len(trinom_list)):
    # grab all of the characters per line that actually contain trinomial data.
    # temporary string variable to store the trinomial.
    tempstr = ""
    for j in range(0, len(trinom_list[i])):
        if trinom_list[i][j].isalpha() or trinom_list[i][j].isdigit():
            tempstr += trinom_list[i][j]
    
    # temporary variable to store a trinomialsplit object
    tempts = ts.TrinomialSplit(tempstr)
    
    #Add the trinomial elements to their respective lists.
    stateList.append(tempts.statenumber)
    countylist.append(tempts.countycode)
    sitelist.append(tempts.sitenumber)


# Write the lists to one CSV file.
with open('separate_tri.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    headerrow = "state,county,row".split(",")
    writer.writerow(headerrow)
    for i in range(0, len(trinom_list)):
        writestring = (str(stateList[i]) + "," + str(countylist[i]) + "," + str(sitelist[i])).split(",")
        writer.writerow(writestring)
        
# isolate_trinomial
# R script to isolate ST's out of a CSV.

#read in the file name as a command line argument.

args <- commandArgs(TRUE)


#Set the command line arg as the filename

filename = as.character(args[1])

# Read in the CSV.

trinomial.set <- read.csv(filename)

trinom.vec <- as.character(trinomial.set$`Trinomial.Instance`)

write(trinom.vec, file = "trinomials.txt", ncolumns = 1)





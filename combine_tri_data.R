# combine_tri_data
# takes original trinomial CSV file in and combines it with the split trinomial CSV file generated 
# separate_trinomial.py. Removes non-trinomials.

# Grab the command line arguments
args <- commandArgs(TRUE)


# Original file is first arg, split trinomials are the second
originalfile <- args[1]
splitfile <- args[2]

# Read in the original.
original.set <- read.csv(original.set)
split.set <- read.csv(splitfile)


# combine_tri_data
# takes original trinomial CSV file in and combines it with the split trinomial CSV file generated 
# separate_trinomial.py. Removes non-trinomials.

# Grab the command line arguments
args <- commandArgs(TRUE)


# Original file is first arg, split trinomials are the second, new data is third.
originalfile <- args[1]
splitfile <- args[2]
newfile <- args[3]

# Read in the original.
original.set <- read.csv(original.set)
split.set <- read.csv(splitfile)

# Make a new data frame.

attach(original.set)
attach(split.set)

(tri_data_split <- data.frame(
  title = Title,
  year = Year,
  volnum = Volume.Number,
  issuenum = Issue.Number,
  pagenum = Page.Number,
  primauth = Primary.Author.s.Last.Name,
  tri_instance = Trinomial.Instance,
  st = state,
  ct = county,
  site = row,
  jstor = JSTOR.LINK,
  ststring = State,
  ctstring = County,
  comm = Comments,
  avoid = Avoid..H.M.L.
))

# Add full combined trinomial back to the data set.
attach(tri_data_split)

tri_data_split$fulltri <- paste(st, ct, site, sep="")

detach(tri_data_split)

detach(original.set)

detach(split.set)

# filter out site codes that take the format of ST's but are in fact not.

attach(tri_data_split)

tri_cleaned <- subset(tri_data_split, ct != "NA", ct != "ML")

detach(tri_data_split)

# write cleaned version to CSV

write.csv(tri_cleaned, newfile)


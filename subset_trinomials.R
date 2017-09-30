# subset_trinomial.r
# R script to make a subset of the trinomials file omitting NA numbers and the Utah strings masquerading as trinomials.
# This will also be implemented in the Python code with rpy2.

trinomials <- read.csv("aa_trinomials.csv")

trinomialscleaned <- subset(trinomials$'Trinomial Instance')





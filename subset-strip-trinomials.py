#Import R packages
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
base = importr('base')

rprint = robjects.r['print']

#read the original CSV data in
read_csv = robjects.r['read.csv']
trinomial_set = read_csv('aa_trinomials.csv')

#make a subset with no NA number of Utah trinomials.

#to be added...









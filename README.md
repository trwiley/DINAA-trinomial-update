# DINAA-trinomial-update

Python and R scripts  written to perform some cleaning work on a dataset of Smithsonian Trinomials taken from American Antiquity issues ranging from 2004 to 2013.

##  What these scripts do

* isolate_trinomials.r takes a CSV with trinomials in and outputs a txt file with only the trinomials in it.
* trinomialsplit.py takes in a string with an ST instance and splits it up into its constituent parts.
* separate_trinomial.py takes in the txt file from isolate_trinomials.R and creates a CSV with the parts of the trinomial in their own
columns.
* combine_tri_data uses the two CSV's and essentially combines them.


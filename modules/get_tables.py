#%%
import pandas as pd
import tabula
import os 

# change the file path to the file needed
file = 'MIL-STD-1472H.pdf'
# update the name of the military standard you are ripping from
target_name = 'MIL-STD-1472H'
# choose directory to save images to
tab_directory = 'MIL-STD-1472H_figures'


#####################################################

# DO NOT CHANGE CODE BELOW THIS POINT

######################################################

# create image directory if it doesn't already exist
if not os.path.exists(tab_directory):
   os.makedirs(tab_directory)

# convert PDF into CSV file
tabula.convert_into(file, "output.csv", output_format="csv", pages='all')
#%%
# change the file path to the file needed
file = 'MIL-STD-1472H.pdf'
# update the name of the military standard you are ripping from
target_name = 'MIL-STD-1472H'
# choose directory to save images to
# tab_directory = 'MIL-STD-1472H_tables'

#####################################################

# DO NOT CHANGE CODE BELOW THIS POINT

######################################################

import os
import pandas as pd
import tabula

# create table directory if it doesn't already exist
# if not os.path.exists(tab_directory):
#    os.makedirs(tab_directory)

# get a placeholder for all the text that we're saving 
dfs = tabula.io.read_pdf(file, 'dataframe', pages='all', stream=True, multiple_tables=True)
# %%

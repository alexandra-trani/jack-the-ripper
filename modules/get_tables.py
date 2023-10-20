#%%
from pdfminer.high_level import extract_text
import re 
import pandas as pd

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


#%%


# list the starting page
page = 43
# list the ending page 
pg_end = 451
# get a placeholder for all the text that we're saving 
text = extract_text(file, 
                    page_numbers=list(range(page,pg_end)))

# replace page header with blank text
text = re.sub(r"MIL-STD-1472H\s*", "", text)
# replace page header with blank text
text = re.sub(r"5.  DETAILED REQUIREMENTS", "", text)
# replace page numbers with blank text
text = re.sub(r"\n\d+ \n", "", text)
# Replace Tables and figures as a section number for quick elimination
text = re.sub(r"TABLE", "5.999 TABLE", text)
text = re.sub(r"FIGURE", "5.999 FIGURE", text)
# get the regex for the id
section_reg = r"\n(?=5\.\d)"
# split the text to a new line 
section = re.split(section_reg, text)

# empty lists 
tag = []
name = []
define = []
# populate empty lists with data from section
for line in section: 
        try:
                lsplit = re.split(r"(?<=.\d)\s+", line)
                tag.append(lsplit[0])
        except:
                tag.append('')
        try:
                second = re.split(r"\.\s+", lsplit[1], 1)
                name.append(second[0])
        except:
                name.append('')
        try:
                second[1] = re.sub(r"\n", "", second[1]) 
                define.append(second[1])
        except:
                define.append('')

# get a list of indices for all tables and figures
indices = [i for i in range(len(tag)) if tag[i] == '5.999']
tf_tag = [item for index, item in enumerate(tag) if index in indices]
tf_name = [item for index, item in enumerate(name) if index in indices]
tf_define = [item for index, item in enumerate(define) if index in indices]
# %%
tf_title = []
tf_cells = []
for title in tf_define:
        lsplit = re.split(r"\.", title)
        tf_title.append(lsplit[0])
        try:
                tf_cells.append(lsplit[1])
        except:
                tf_cells.append("")
# %%

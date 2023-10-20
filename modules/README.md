# 1472H-extractor
Extract text from 1472H with ease! 

As it stands, the extractor file pulls all the section headers, sections, and numeric identification from Chapter 5 of 1472H.
Tables and figures are all identified as 5.999.

## CSV Columns Extracted
| Column Name | Description |
| ----------- | ----------- |
| Tag | Numerical reference to the chapter.section instance of the standard. |
| Name | Name of the standard. |
| Definition | if a definition exists, this is the definition	of the standard. |
| MIL-STD	| Name of the MIL-STD document from which these standards are derrived. |
| ID | Unique identifier or primary key built by combining the MIL-STD and the tag. |

## Future Work
I am in the process of converting this into a quick python function for easy calling at a later date. 

# get_img_from_pdf
Fast ripper to pull images from a pdf, save them to a directory, and index the page numbers and the image on the page while doing it. 

## Next Steps: 
Create user interface so that this is ultimately user friendly! 
Link with Extractor.py code so that they can work in tandem. 

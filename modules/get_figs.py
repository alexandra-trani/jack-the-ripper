from PIL import Image
import fitz
import io
import os 

# change the file path to the file needed
file = 'MIL-STD-1472H.pdf'
# update the name of the military standard you are ripping from
target_name = 'MIL-STD-1472H'
# choose directory to save images to
img_directory = 'MIL-STD-1472H_figures'


#####################################################

# DO NOT CHANGE CODE BELOW THIS POINT

######################################################

# create image directory if it doesn't already exist
if not os.path.exists(img_directory):
   os.makedirs(img_directory)

# load the pdf file
pdf_file = fitz.open(file)
with open(f'{target_name}_readme.txt', 'w') as f:
    for page_index in range(len(pdf_file)):
        # get the page itself
        page = pdf_file[page_index]
        image_list = page.get_images()
        # printing number of images found in this page
        if image_list:
            line = f"[+] Found a total of {len(image_list)} images in page {page_index}"
        else:
            line = f"[!] No images found on page {page_index}"
        f.write(line)
        f.write('\n')

    for image_index, img in enumerate(page.get_images(), start=1):
        # get the XREF of the image
        xref = img[0]
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        image.save(f"{img_directory}/{target_name}_{page_index+1}_{image_index}.jpeg")
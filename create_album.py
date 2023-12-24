import os
from airium import Airium
import sys

# Get the folder name from the command line argument, or use the current folder as default
if len(sys.argv) > 1:
  folder = sys.argv[1]
  output = os.path.basename(folder) + ".html"
else:
  folder = "./"
  output = 'all.html' # The name of the output file

images = [] # Create an empty list for the images
for file in os.listdir(folder): # Loop through the files in the folder
  if file.endswith('.jpg'): # Check if the file is a jpg image
    images.append(file) # Append the file name to the images list

a = Airium() # Create an HTML document object

for image in images: # Loop through the images
  with a.div():
    a.img(src=f'{folder}/{image}')

html_str = str(a)

with open(output, 'w') as f:
    f.write(html_str)
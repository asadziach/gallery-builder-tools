#!/usr/bin/env python3

import os
from bs4 import BeautifulSoup
import sys

# Get the folder name from the command line argument, or use the current folder as default
if len(sys.argv) > 1:
  folder = sys.argv[1]
  output = os.path.basename(folder) + ".html"
else:
  folder = "./"
  output = 'all.html' # The name of the output file

image_suffixes = ('jpg','jpeg', 'jfif', 'pjpeg', 'pjp', 
                   'gif', 'png', 'apng', 'avif', 'svg', 'webp')
video_suffixes = ('mp4','webm', 'ogg')
images = [] # Create an empty list for the images
videos = [] # Create an empty list for the videos
for file in os.listdir(folder): # Loop through the files in the folder
  if file.endswith(image_suffixes): # Check if the file is a jpg image
    images.append(file) # Append the file name to the images list
  elif file.endswith(video_suffixes):
    videos.append(file) # Append the file name to the images list

soup = BeautifulSoup("<b></b>", "html.parser")
original_tag = soup.b

for image in images: # Loop through the images
  new_tag = soup.new_tag("img", src=f'{folder}/{image}')
  original_tag.append(new_tag)

for video in videos: # Loop through the videos
  new_tag = soup.new_tag("video controls", src=f'{folder}/{video}')
  original_tag.append(new_tag)

html_str = soup.prettify()

with open(output, 'w') as f:
    f.write(html_str)
    print(output, "Ready.")
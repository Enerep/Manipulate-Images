import os, sys
from PIL import Image

yourdir = input("Where you want to save your images?: ")
fileformat = input("What format do you want it to be?(JPEG, PNG, JPG): ")
rotation = input("How much you want to rotate your image?(<360): ")


for root, dirs, files in os.walk("."):
  for file in files:
    f, e = os.path.splitext(file)
    outfile = yourdir + f
    try:
      #print(outfile)
      Image.open(file).rotate(rotation).resize((640,480)).convert("RGB").save(outfile, fileformat)

    except IOError:
      print("cannot convert", file)
  

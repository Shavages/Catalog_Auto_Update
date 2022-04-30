#!/usr/bin/env python3

from email.mime import image
import os, sys
from PIL import Image
import glob

file = './supplier-data/images/001.tiff'

def get_files():
    file_location  = os.path.join(os.getcwd(),'supplier-data', 'images', '*.tiff')
    filenames = glob.glob(file_location)
    return filenames


def convert_image(inFile):
    f, e = os.path.splitext(inFile)
    outFile = f + ".jpeg"
    if inFile != outFile:
        try:
            with Image.open(inFile) as im:
                im = im.convert("RGB")
                im = im.resize((600,400))
                im.save(outFile, "JPEG")
        except OSError:
            pass
    

def main():
    files = get_files()
    for file in files:
        convert_image(file)

if __name__ == "__main__":
    main()
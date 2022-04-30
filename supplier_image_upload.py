#!/usr/bin/env python3

import glob
import os
import requests

url = "http"

def get_files():
    file_location  = os.path.join(os.getcwd(),'supplier-data', 'images', '*.jpeg')
    filenames = glob.glob(file_location)
    return filenames


def upload_images(filesList):
    url = "http://localhost/upload/"
    for file in filesList:
        with open(file, "rb") as opened:
            r = requests.post(url, files={'file', opened})

def main():
    files = get_files()
    print(files)

if __name__ == "__main__":
    main()


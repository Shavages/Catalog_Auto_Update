#!/usr/bin/env python3

from base64 import decode
from distutils.log import error
import glob
import os
import requests

def get_files():
    file_location  = os.path.join('.','supplier-data', 'descriptions', '*.txt')
    filenames = glob.glob(file_location)
    return filenames

def process_file(file):
    file_name = file.strip('./supplier-data/descriptions/')
    descrip_dic = {}
    with open(file, 'rb') as f:
        lines = f.readlines()
    descrip_dic['name'] = lines[0].strip().decode()
    descrip_dic['weight'] = int(lines[1].strip().decode().replace(" lbs", ""))
    descrip_dic['description'] = lines[2].strip().decode()
    descrip_dic['image_name'] = file_name.replace('tx', 'jpeg')
    return descrip_dic
    
    
def upload_dic(descrip):
    external_ip = ""
    url = "http://{}/fruits".format(external_ip)
    r = requests.post(url, json=descrip)
    if r.status_code != 200:
        raise error("Error: description not posted. Description: {}".format(descrip))

def upload_process(files):
    for file in files:
        descrip_dic = process_file(file)
        upload_dic(descrip_dic)


def main():
    files = get_files()
    upload_process(files)

if __name__=="__main__":
    main()

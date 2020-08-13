#!/usr/bin/env python3
import requests
import os

url="http://localhost/upload/"
directory_path="supplier-data/images" #Where the .jpeg images are stored
for each_file in os.listdir(directory_path):
    if ".jpeg" in each_file:
        with open("{}/{}".format(directory_path,each_file),"rb") as file:
            r = requests.post(url,files={'file':file})
            print(r.status_code)
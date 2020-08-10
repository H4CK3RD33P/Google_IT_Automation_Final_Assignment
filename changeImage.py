#!/usr/bin/env python3

from PIL import Image
import os

directory_path="supplier-data/images" #directory where all the supplier images are stored

for each_file in os.listdir(directory_path): #goes through each of the files inside the directory
	if ".tiff" in each_file: #To just modify the .tiff files
		imgname,oldext=each_file.split(".")
		newfile=imgname+".jpeg" #changes the name to imagename.jpeg
		img=Image.open("{}/{}".format(directory_path,each_file))
		img.convert("RGB").resize((600,400)).save("{}/{}".format(directory_path,newfile,"jpeg")) 
		#converts images to RGB, resizes and saves it to .jpeg format
#!/usr/bin/env python3
import requests
import os

def process_txt():
    directory_path="supplier-data/descriptions"
    field=['name','weight','description','image_name']
    process_dict_list=[]
    for each_file in os.listdir(directory_path):
        if ".txt" in each_file:
            count=0
            process_dict={}
            with open("{}/{}".format(directory_path,each_file)) as file:
                for line in file:
                    if field[count]=='name' or field[count]=='description' :
                        process_dict[field[count]]=line.strip('\n')
                    if field[count]=='weight':
                        process_dict['weight']=int(line.strip('\n').strip(' lbs'))
                    count+=1
                name,_=each_file.split('.')
                img=name+'.jpeg'
                process_dict['image_name']=img    
            process_dict_list.append(process_dict)
    return process_dict_list

if __name__ == "__main__":
    url="http://localhost/fruits/"
    process_dict_list=process_txt()
    for process_dict in process_dict_list:
        response=requests.post(url,json=process_dict)
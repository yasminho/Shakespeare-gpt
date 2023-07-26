import pandas as pd
#requests is a popular python libarary for making HTTP requests, such as downloading from URLs
import requests

## Download the dataset to train on
url='https://raw.githubusercontent.com/yasminho/Shakespeare-gpt/main/input.txt'
response=requests.get(url)

#we need to check the status_code
#if the status_code is 200 thi smean that it was successful download 
#if it is any other error, it was not a successful download 
if response.status_code==200:
    text=response.text 
else: 
    raise Exception("did not download")


#I need to read it in 
#'r' means read mode 
#the encoding specifies that the file should be read using the UTF-8 encoding, which is common for text files 


with open('input.txt', 'r', encoding='utf-8') as f:
    text=f.read()

print(len(text))

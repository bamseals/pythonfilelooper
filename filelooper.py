import os
from os.path import isfile

#path format example: /Users/Sam/Downloads/Movies' 

path = input('Input path to folder: ')
os.chdir(path)

count = 0
for f in os.listdir():
    if isfile(f):
        count += 1
        print(f)
    
if count == 0:
    print('No files in folder')
    quit()
else:
    operation = input('Add or remove from these filenames? ')
    if 'add' != operation.lower() and 'remove' != operation.lower():
        print('incorrect input')
        quit()
    else:
        text = input ('What would you like to '+operation+'? ')    
        for f in os.listdir():
            if isfile(f):
                if 'add' == operation.lower():
                    splitstring  = f.split('.')
                    splitstring[0]+=text
                    new_name = '.'.join(splitstring)
                elif 'remove' == operation.lower():
                    new_name = f.replace(text,'')
                os.rename(f,new_name)
                print(new_name)
        
    

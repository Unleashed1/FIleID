import os
import json
file_path = os.getcwd() ##path filejson
path = os.getcwd()+'\FileFolder'
filelist = os.listdir(path)
index = 0 
out = []
l = []
l = filelist 
for el in filelist :
    abspath = os.path.abspath(path) # path file for the examination
    data = json.loads(open(os.path.join(file_path, file_path+"/data.json"), "r",encoding = "utf-8").read())
    file = open(path+'/'+el, "rb").read(32) #to mod
    hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])
    
    for element in data:
        for signature in element["signature"]:
            offset = element["offset"]*2+element["offset"]
            if signature == hex_bytes[offset:len(signature)+offset].upper():
                out.append(element["extension"])
 
#i'm going to add the automatic aquisition of the paths and the restore sistem for all  the files in the directory
os.chdir(os.getcwd()+'\FileFolder')
for elem in filelist:
    #os.rename(path+'/'+elem,'file'+str(index)+'.'+out[index+1])
    os.rename(path+'/'+elem,elem+'.'+out[index+1])

    if(index == len(filelist)):
        break
    index= index+2

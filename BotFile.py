import os
import json
file_path = os.getcwd() ##path filejson
filelist = os.listdir(os.getcwd())

out = []

for el in filelist :
    print(el)
    abspath = os.path.abspath(file_path) # path file for the examination
    data = json.loads(open(os.path.join(abspath, file_path+"/data.json"), "r",encoding = "utf-8").read())
    file = open(file_path+'/'+el, "rb").read(32) #to mod
    hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])
    
    for element in data:
        for signature in element["signature"]:
            offset = element["offset"]*2+element["offset"]
            if signature == hex_bytes[offset:len(signature)+offset].upper():
                out.append(element["extension"])
print(out) #to mod 
#i'm going to add the automatic aquisition of the paths and the restore sistem for all  the files in the directory

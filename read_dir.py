##
##
## GPL to Generate all the files in each folder.
##
##
import os 
l=os.listdir("/home/unimauro/Develop/TDD-KATA") 

for i in l:
    if i.find(".")<0:
            print(i)
            l=open(i+"/Readme.md","w")
            l.writelines(i.upper())
            l.close()


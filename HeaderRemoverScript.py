#Gattling HAR - Header Remove Script
#by ap01z

import os
import re
import time 
import sys
#enter your directory by replacing FolderName below.
#ensure all files are in scala format. no .txt 

start = time.time()
if len(sys.argv) < 2:
    print("Add folder name or edit the script; eg: 'python remover.py folderName' ")
    exit(0)
else:
    var = sys.argv[1]
    for subdir, dirs, files in os.walk(var):
        for filename in files:
            filepath = subdir + os.sep + filename

            if filepath.endswith(".scala") :
                print (filepath)

                with open(filepath, "r") as lol:
                    
                    lines = lol.readlines()

                with open(filepath, "w") as lol:
                    
                    for line in lines:
                        
                        if (re.search("val.head",line)):
                            print("line val removed") #you can comment this to avoid spam
                            #countval = countval + 1

                        elif (re.search("->",line)):
                            print("line -> removed") #you can comment this to avoid spam
                        
                        elif (re.search("\.headers\(headers_\d{1,3}\)",line)):
                            lol.write(re.sub("\.headers\(headers_\d{1,3}\)","",line))
                            print("removed headers") #you can comment this to avoid spam

                        else:
                            #print(line) #you can comment this to avoid spam
                            lol.write(line)
            
            print("Headers Removed - Done")

    end = time.time() #fancy stuff, not important

    print(end-start)
    print("seconds elapsed") #fancy stuff, not important
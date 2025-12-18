'''
WK-3 STARTER SCRIPT

'''

# Python Standard Libaries 
import os
import hashlib
import time



# Python 3rd Party Libraries
from prettytable import PrettyTable     # pip install prettytable

# Psuedo Constants

targetFolder = input("Enter Target Folder: ")

# Start of the Script

print("Walking: ", targetFolder, "\n")

tbl = PrettyTable(['AbsPath','Type', 'FileSize', 'UTC-Modified', 'UTC-Accessed', 'UTC-Created', 'SHA-256 HASH'])  

for currentRoot, dirList, fileList in os.walk(targetFolder):

    for nextFile in fileList:
        
        fullPath = os.path.join(currentRoot, nextFile)
        absPath  = os.path.abspath(fullPath)
        
        if os.path.isfile(absPath):
            fileType = "file"
        elif os.path.isdir(absPath):
            fileType = "Directory"
        elif os.path.islink(absPath):
            fileType = "link"
        else:
            fileType = "unknown"
            
        fileSize = os.path.getsize(absPath)
        stats = os.stat(absPath)
        timeLastModified = stats.st_mtime
        humanTimeLastModified = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastModified))        
        timeLastAccess   = stats.st_atime
        humanTimeLastAccess = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastAccess))
        timeLastCreated = stats.st_ctime
        humanTimeLastCreated = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastCreated))
        
        with open(absPath, 'rb') as target:
            
            fileContents = target.read()
            
            sha256Obj = hashlib.sha256()
            sha256Obj.update(fileContents)
            hexDigest = sha256Obj.hexdigest() 
            
        tbl.add_row([ absPath, fileType, fileSize, humanTimeLastModified, humanTimeLastAccess, humanTimeLastCreated, hexDigest])
        
        
        
tbl.align = "l" # align the columns left justified
# display the table
print (tbl.get_string(sortby="FileSize", reversesort=True))


print("\nScript-End\n")
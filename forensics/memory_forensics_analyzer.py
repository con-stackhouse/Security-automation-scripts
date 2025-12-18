'''
Connor S
Final Script
May 2024
'''
import re

print("Final Script")
with open("mem.raw", 'rb') as target:  # assumes that mem.raw is in the same folder as script
    
    contents = target.read() # read the entire contents of the file
    
    txt = re.sub(b"[^A-Za-z']", b' ', contents)  # strip all non alpha characters
    txt = txt.lower()                            # convert all to lower case
    txt = txt.decode("utf-8")                    # convert to simple ASCII
    
    wordList = txt.split()  # Create a list of possible words
    print(len(wordList))
    
    wordCount = {}
    overlap = b''
    chunkSize = 65535
    
with open("mem.raw", 'rb') as target:    
    while True:          
        fileChunk = target.read(chunkSize)
        if fileChunk:  
            fileChunk = overlap + fileChunk
            txt = re.sub(b"[^A-Za-z']", b' ', fileChunk)  
            txt = txt.lower()                                 
            txt = txt.decode("utf-8")                         
            wordList = txt.split()                           
                    
            for word in wordList:
                if word in wordCount:
                    wordCount[word] += 1
                else:
                    wordCount[word] = 1 
            overlap = fileChunk[-20:]
        else:
            print("\nFile Processed:", target.name)
            break 
            
    kernelCount = wordCount.get("kernel", 0)
    encryptCount = wordCount.get("encrypt", 0)
    fairwitnessCount = wordCount.get("fairwitness", 0)
        
    
    print("kernelCount: ",      kernelCount)
    print("encryptCount:",      encryptCount)
    print("fairwitnessCount: ", fairwitnessCount)
    

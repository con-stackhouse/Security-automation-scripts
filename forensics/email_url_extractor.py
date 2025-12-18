'''Email & URL Extractor from Memory DumpsAuthor: Connor StackhouseCourse: Cyber Operations Engineering - University of Arizona  Date: September 2024Purpose:    Extracts email addresses and URLs from binary memory dumps using    regular expressions. Performs frequency analysis to identify    significant communication artifacts.Security Application:    - Memory forensics    - Investigation of communication patterns    - Data exfiltration detection    - Network artifact recoveryUsage:    python3 email_url_extractor.py    (Prompts for memory dump file and chunk size)Requirements:    - Python 3.x    - prettytable: pip install prettytableOutput:    - Sorted tables of email addresses by frequency    - Sorted tables of URLs by frequency'''import os
import re
import sys
from binascii import hexlify 
from prettytable import PrettyTable

print("\nExtract e-mails and urls from the memory dump provided\n")

try:
    # Prompt for file to process and chunk size 
    largeFile = input("Enter the name of the memory dump file: ")
    chunkSize = int(input("What size chunks?  "))

    # Regular expression patterns 
    ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')
    uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')        
    wPatt = re.compile(b'[a-zA-Z]{5,15}')  
    
    emailList = []
    urlList = []
    wordList = []
    emailDict = {}
    urlCount = {}
    wordDict = {}

    if os.path.isfile(largeFile):
        overlap = b''

        with open(largeFile, 'rb') as binaryFile:
            while True:
                fileChunk = binaryFile.read(chunkSize)
                if fileChunk:
                    fileChunk = overlap + fileChunk

                    
                    emailMatches = ePatt.findall(fileChunk)
                    for eachEmail in emailMatches:
                        eachEmail = eachEmail.decode()
                        emailList.append(eachEmail)
                        if eachEmail in emailDict:
                            emailDict[eachEmail] += 1
                        else:
                            emailDict[eachEmail] = 1

                    
                    urlMatches = uPatt.findall(fileChunk)
                    for eachURL in urlMatches:
                        eachURL = eachURL.decode()
                        urlList.append(eachURL)
                        if eachURL in urlCount:
                            urlCount[eachURL] += 1
                        else:
                            urlCount[eachURL] = 1
                            
                    wordMatches = wPatt.findall(fileChunk)
                    for eachWord in wordMatches:
                        eachWord = eachWord.decode()
                        wordList.append(eachWord)
                        if eachWord in wordDict:
                            wordDict[eachWord] += 1
                        else: 
                            wordDict[eachWord] = 1

                    # Manage overlap for next chunk
                    overlap = fileChunk[-20:]  # Adjust overlap size based on chunk size
                else:
                    print("\nFile Processed:", largeFile)
                    print("\nResult Tables:")
                    break

        # Display results 
        emailTable = PrettyTable(["OCCURS", "EMAIL"])
        for key, value in emailDict.items():
            emailTable.add_row([value, key])
        emailTable.align = 'l'
        print("\nEmails Found:")
        print(emailTable.get_string(sortby="OCCURS", reversesort=True))

        urlTable = PrettyTable(["OCCURS", "URL"])
        for key, value in urlCount.items():
            urlTable.add_row([value, key])
        urlTable.align = 'l'
        print("\nURLs Found:")
        print(urlTable.get_string(sortby="OCCURS", reversesort=True))
        
        wordTable = PrettyTable(["OCCURS", "WORD"])
        for key, value in wordDict.items():
            wordTable.add_row([value, key])
        wordTable.align = 'l'
      #  print("\nWords Found:")
      #  print(wordTable.get_string(sortby="OCCURS", reversesort=True))
        

    else:
        print(largeFile, "is not a valid file")
        sys.exit("Script Aborted")

except Exception as err:
    sys.exit("\nException: " + str(err) + " Script Aborted")

print("\nFile Processed ... Script End")

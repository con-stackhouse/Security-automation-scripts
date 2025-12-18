'''Memory Dump String Frequency AnalyzerAuthor: Connor StackhouseCourse: Cyber Operations Engineering - University of ArizonaDate: September 2024Purpose:    Extracts text strings from binary memory dumps and performs    frequency analysis to identify significant patterns and keywords.Security Application:    - Memory forensics    - Malware analysis (identifying suspicious strings)    - Artifact recovery from RAM    - Pattern recognition in memory dumpsUsage:    python3 memory_string_analyzer.py    (Processes mem.raw file in current directory)Requirements:    - Python 3.x    - prettytable: pip install prettytable    - mem.raw file in same directoryOutput:    Top 50 most frequent text strings found in memory'''import re
import os 
import sys
from prettytable import PrettyTable

# File Chunk Size 
CHUNK_SIZE = 1024

# Regular expression for continuous alpha string pattern
wPatt = re.compile(b'[a-zA-Z]{5,15}')

# Dictionary to store word occurrences
wordCount = {}

# Read the binary file with an overlap 
overlap = b''
with open('mem.raw', 'rb') as binaryFile:
    while True:
        chunk = binaryFile.read(CHUNK_SIZE)
        if chunk:
            chunk = overlap + chunk 
            wordMatches = wPatt.findall(chunk)
            
            for eachWord in wordMatches:
                eachWord = eachWord.decode()
                if eachWord in wordCount:
                    wordCount[eachWord] += 1
                else:
                    wordCount[eachWord] = 1
                    
            overlap = chunk[-20:]
        else:
            break  


print("\nFile Processed:", 'mem.raw')

# Display results 
wordTable = PrettyTable(["OCCURS", "WORD"])
for key, value in wordCount.items():
    wordTable.add_row([value, key])
wordTable.align = 'l'
wordTable.sortby = "OCCURS"
wordTable.reversesort = True  

topResults = 50
print("\nTop Unique Strings Found:")
print(wordTable.get_string(start=0, end=topResults))

print("\nFile Processed ... Script End")


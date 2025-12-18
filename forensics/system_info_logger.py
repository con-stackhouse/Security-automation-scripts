'''
System Information Forensic Logger
Author: Connor Stackhouse
Course: Cyber Operations Engineering - University of Arizona
Date: October 2024

Purpose:
    Comprehensive system profiling tool that collects system information
    and generates forensic file catalog with SHA-256 hashes.

Security Application:
    - Forensic system profiling
    - Incident response documentation
    - Evidence collection
    - System baseline creation
    - Chain of custody preparation

Usage:
    python3 system_info_logger.py
    (Prompts for investigator name and target folder)

Requirements:
    - Python 3.x
    - psutil: pip install psutil

Output:
    Creates detailed log file (system_info_logger.txt) containing:
    - Investigator information
    - Complete system profile (OS, hardware, network)
    - SHA-256 file catalog with timestamps
    - File count summary
    
Note:
    Output log file serves as forensic documentation for investigations

'''

import os
import re
import logging
import platform
import socket
import uuid
import hashlib
import time

import psutil  

def getSystemInfo():
    try:
        info = {}
        info['    platform'] = platform.system()
        info['    platform-release'] = platform.release()
        info['    platform-version'] = platform.version()
        info['    architecture'] = platform.machine()
        info['    hostname'] = socket.gethostname()
        info['    ip-address'] = socket.gethostbyname(socket.gethostname())
        info['    mac-address'] = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['    processor'] = platform.processor()
        info['    ram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False


def main():
    
    # Remove any old logging script
    if os.path.isfile('Stackhouse-Connor-Wk-6.txt'):   
        os.remove("Stackhouse-Connor-Wk-6.txt")
    
    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='Stackhouse-Connor-Wk-6.txt', level=logging.DEBUG, format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")
    
    investigator = input("Investigator Name:  ")   
    organization = input("Class Code  :       ")   
    
    logging.info("Investigator Name:  " + investigator)
    logging.info("Class Code:  " + organization)
    logging.info("\n")
    sysInfo = getSystemInfo()
    
    if sysInfo:
        
        logging.info("    System Information   ")
        
        for key, value in sysInfo.items():
            logging.info(key + ": " + str(value))
        logging.info("\n")
        
        
        targetFolder = input("Enter a specified folder: ")
        filesProcessed = 0 
        
        
        for currentRoot, dirList, fileList in os.walk(targetFolder):
            for nextFile in fileList:
                filePath = os.path.join(currentRoot, nextFile)
                
                
                try:
                    with open(filePath, 'rb') as target:
                        fileContents = target.read()
                        sha256Obj = hashlib.sha256()
                        sha256Obj.update(fileContents)
                        hexDigest = sha256Obj.hexdigest()                        
                except Exception as e:
                    logging.exception(e)
                    hexDigest = None
                
                stats = os.stat(filePath)
                fileSize = os.path.getsize(filePath)
                
                
                timeLastModified = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(stats.st_mtime))
                timeLastAccess = stats.st_atime
                humanTimeLastAccess = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastAccess))
                timeLastCreated = stats.st_ctime
                humanTimeLastCreated = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(timeLastCreated))
                
                filesProcessed += 1 
                
                logging.info("    File Path: " + filePath)
                logging.info("    File Size: " + str(fileSize))
                logging.info("    Last Modified Time: " + timeLastModified)
                logging.info("    Last Accessed Time: " + humanTimeLastAccess)
                logging.info("    Last Created Time: " + humanTimeLastCreated)
                logging.info("    SHA256 Hash: " + hexDigest)
                logging.info("\n")
            
    logging.info("Files Processed: " + str(filesProcessed))      

if __name__ == '__main__':
    
    print("\n\nWeek-6 Logging Starter Script - Connor \n")
    main()
    print("\nScript End")

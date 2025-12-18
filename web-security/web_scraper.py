'''Web Scraper & Reconnaissance ToolAuthor: Connor StackhouseCourse: Cyber Operations Engineering - University of ArizonaDate: October 2024Purpose:    Extracts links and downloads images from websites for security    assessment and reconnaissance. Demonstrates web scraping for OSINT.Security Application:    - Web application reconnaissance    - OSINT (Open Source Intelligence)    - Website enumeration    - Asset discoveryUsage:    python3 web_scraper.py    (Modify URL variable in script before running)Requirements:    - Python 3.x    - requests: pip install requests    - beautifulsoup4: pip install beautifulsoup4    - Pillow: pip install PillowOutput:    - Downloaded images saved to specified directory    - List of all links found on page    Note:    Only use on websites you have permission to scan.'''import requests                       # Pthon library for url requests 
import os 
from bs4 import BeautifulSoup         # 3rd party BeautifulSoup library
from PIL import Image                 # 3rd party Python Image library 
from io import BytesIO                 

URL = 'https://casl.website'
saveImg = 'D:/images/'
# retireve web page from instructions
page = requests.get(URL)

# convert the page into a beautifulsoup object for processing 
soup = BeautifulSoup(page.text, 'html.parser')       

pageTitle = soup.title
pageLinks = set()
imgLinks = set()

linkTags = soup.findAll('a')

if soup.title is not None:  
    pageTitle = soup.title.string  
else:
    pageTitle = 'No title found'  
print("Page Title: " + pageTitle)
print()

if linkTags:
    for eachLink in linkTags:
        newLink = eachLink.get('href')
        
        if not newLink:
            continue
        
        if 'http' not in newLink:
            newLink = URL + newLink
        pageLinks.add(newLink)
 
imageTags = soup.findAll('img')       
if imageTags:
    for eachImage in imageTags:
        try: 
            imgURL = eachImage['src']
            
            # display the url of the image 
            print("Image URL:  ", imgURL)
            
            # display the alternative text associated with the image 
            print("Alt text: ", eachImage.get('alt', 'no alt text provided'))
            if imgURL[0:4] != 'http':   # if URL path is relative
                imgURL = URL + imgURL    # prepending base url 
            response = requests.get(imgURL)  # Get image fromt the URL 
            imageName = os.path.basename(imgURL)  
            img = Image.open(BytesIO(response.content))  # Download the image 
            img.save(os.path.join(saveImg, imageName))  # Save the image
                
            print("Downloaded " + imageName)  
                
        except Exception as err:
            print("Error with image URL:", imgURL, err)
            
print("\nPage Links:")
for eachLink in pageLinks: 
    print(eachLink)
    

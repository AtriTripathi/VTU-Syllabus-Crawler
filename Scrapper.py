# Make sure you have pip installed BeautifulSoup4 and also lxml parser.
# See if you can find any logic to print Unit names and there Descriptions together.
# Also there are reference book visible. Can't figure out how to remove it.

from bs4 import BeautifulSoup
import re

url = r"C:\Users\Atri\Downloads\assets\AL_12_10CCP13_10CCP23_C_PROGRAMMING.html"  # Use the path of html file
                                                                                  # and don't remove 'r'
page = open(url)
soup = BeautifulSoup(page.read(), "lxml")

print(soup.h1.text)  # To Scrape the subject name

strings = soup.find_all(string=re.compile('Subject Code'))  # These many lines just to scrape Subject Code
for txt in strings:
    print(" ".join(txt.split()))

for unit in soup.find_all('h3'):  # To scrape the Unit names
    print(unit.text)

for des in soup.find_all('p'):  # To scrape Descriptions of Units
    print(des.text)
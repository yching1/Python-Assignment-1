from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.buzzfeed.com/")
ReadHeader = BeautifulSoup(html.read(),'html.parser');
print(ReadHeader.h1)
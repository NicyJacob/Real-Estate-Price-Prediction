import pandas as pd
import requests
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from time import perf_counter

sart_time = perf_counter()

url = "https://www.immoweb.be/sitemap.xml"
response = requests.get(url)
soup = BeautifulSoup(response.text,"xml")
#print(soup.prettify())
details=[]
for detail in soup.find_all("loc"):
    details.append(detail.text)
print("details")
links =[]
for link in details:
    #print(link)
    if link.startswith("https://assets.immoweb.be/sitemap/classifieds"):
        links.append(link)
property_list = []
for classified in links:
    property_links = requests.get(classified)
    soup1 = BeautifulSoup(property_links.text,"xml")
    #print(soup1.prettify())
    substring = "https://www.immoweb.be/en"
    for property_link in soup1.find_all("loc"):
        #print(property_link)
        check = property_link.text
        if substring in check:
            property_list.append(property_link)
        else:
            continue
print(len(property_list))
print(f" \n Time in execution = {perf_counter()-start_time} seconds")  

        

    


    


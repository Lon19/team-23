import requests
from bs4 import BeautifulSoup
import csv

#


URL = "https://www.ucas.com/events/2020-entry-deadline-universities-oxford-and-cambridge-and-most-courses-medicine-veterinary-348816"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())
row = soup.find('meta', attrs={'name': 'expires'})
print(row['content'])


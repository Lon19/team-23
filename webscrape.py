import requests
from bs4 import BeautifulSoup
import csv

#
# URL = "https://www.undergraduate.study.cam.ac.uk/events/cambridge-open-days"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')
# deadlineDates = []
# #print(soup.prettify())
#
# table = soup.find('head')
# # print(table.prettify())
#
# # for row in table.findAll('meta', attrs={'name', 'description'}):
# #     print(row)
#
# row = soup.find('meta', attrs={'name': 'description'})
# print(row['content'])
# deadlineDates['Cambridge'] = row['content']
#
#
# # for row in table .findAll('meta', attrs = {'name': 'dcterms.description'}):
# #         deadlineDates = {}
# #         deadlineDates['Cambridge'] = row.content
#
#
# print(deadlineDates)
#
#

# URL = "https://www.undergraduate.study.cam.ac.uk/applying/ucas-application"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')
# #print(soup.prettify())
# row = soup.find('meta', attrs={'name': 'description'})
# print(row['content'])


URL = "https://www.ucas.com/events/2020-entry-deadline-universities-oxford-and-cambridge-and-most-courses-medicine-veterinary-348816"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
#print(soup.prettify())
row = soup.find('meta', attrs={'name': 'expires'})
print(row['content'])


# URL = "https://www.undergraduate.study.cam.ac.uk/courses/computer-science"
# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html5lib')
# grades = []
# print(soup.prettify())
# print(soup.find('id'='entry-requirements'))

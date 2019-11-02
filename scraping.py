import requests
from bs4 import BeautifulSoup

URL = "https://www.undergraduate.study.cam.ac.uk/courses/computer-science"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

req = [td.find_next('p') for td in soup.find(id="entry-requirements")]
sample = req[0].get_text()
a_level,ib = sample.split("IB",1)
print (a_level)
ib = sample.replace(a_level,'')
print(ib)
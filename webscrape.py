import requests
from bs4 import BeautifulSoup
import csv

def parser(dealine):
    message = """<html>
    <head></head>
    <p>The Deadline for Applications to Cambridge University is</p>
    <p>"{0}"</p>
    </html>
    """.format(dealine)
    return message

def get_deadline():
    URL = "https://www.ucas.com/events/2020-entry-deadline-universities-oxford-and-cambridge-and-most-courses-medicine-veterinary-348816"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    #print(soup.prettify())
    row = soup.find('meta', attrs={'name': 'expires'})
    deadline = row['content']
    return parser(deadline=deadline)


import pickle
import requests
from bs4 import BeautifulSoup
import csv


class Basket:

    def __init__(self):
        self.mylist = self.reload()

    def tradeBoard(self, currentboard, newboard):
         self.removeboard(currentboard)
         self.addboard(newboard)

    def save(self):
        with open(r'persistence.pkl', 'wb') as f:
            pickle.dump(self.mylist, f, pickle.HIGHEST_PROTOCOL)

    def addboard(self, board):
        self.mylist.append(board)
        self.save()

    def removeboard(self, board):
        self.mylist.remove(board)
        self.save()

    def reload(self):
        with open(r'persistence.pkl', 'rb') as f:
            return pickle.load(f)

class Board:

    university = ""
    keyDates = {}

    def __init__(self, university, kwargs):
        self.university = university
        self.keyDates = kwargs


class Pagepuller:

    def __init__(self):
        pass

    def createBoard(self, university):
        board = Board(university, {'deadline': self.deadline()})
        return board


    def deadline(self):
        URL = "https://www.ucas.com/events/2020-entry-deadline-universities-oxford-and-cambridge-and-most-courses-medicine-veterinary-348816"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        row = soup.find('meta', attrs={'name': 'expires'})
        return row['content']

    def createBoard(self, university):
        board = Board(university, {'deadline': self.deadline()})
        return board



def parser(a_level, ib):
    message = """<html>
    <head></head>
    <p>The Requirements for Cambridge University</p>
    <p>"{0}"</p>
    <p>"{1}"</p>
    </html>
    """.format(a_level, ib)
    print(message)


def requirements(url):
    URL = url
    r = requests.get(URL)
    print("The entry requirements for " + " are:")
    soup = BeautifulSoup(r.content, 'html.parser')

    temp = [td.find_next('p') for td in soup.find(id="entry-requirements")]
    requirement = temp[0].get_text()
    a_level, ib = requirement.split("IB")
    print(a_level)
    ib = requirement.replace(a_level, '')
    print(ib)
    return parser(a_level=a_level, ib=ib)


def get_requirements():
    course_hashmap = {"Computer Science": "https://www.undergraduate.study.cam.ac.uk/courses/computer-science",
                      "Chemical Engineering": "https://www.undergraduate.study.cam.ac.uk/courses/chemical-engineering",
                      "Mathematics": "https://www.undergraduate.study.cam.ac.uk/courses/mathematics"
                      }
    input_course = "Mathematics"
    return requirements(course_hashmap.get(input_course))


def test_page():
    page = Pagepuller()
    basket = Basket()
    basket.addboard(page.createBoard("Cambridge"))
    for x in basket.mylist:
        print(x)
        print(x.university)
        print(x.keyDates)


test_page()

get_requirements()
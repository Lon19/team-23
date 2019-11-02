import requests
from bs4 import BeautifulSoup

def parser(a_level,ib):
    message="""<html>
    <head></head>
    <p>The Requirements for Cambridge University</p>
    <p>"{0}"</p>
    <p>"{1}"</p>
    </html>
    """.format(a_level,ib)
    print(message)

def requirements(url):
    
    URL = url
    r = requests.get(URL)
    print("The entry requirements for " + " are:")
    soup = BeautifulSoup(r.content, 'html.parser')

    temp = [td.find_next('p') for td in soup.find(id="entry-requirements")]
    requirement = temp[0].get_text()
    a_level,ib = requirement.split("IB")
    print (a_level)
    ib = requirement.replace(a_level,'')
    print(ib)
    return parser(a_level=a_level,ib=ib)

def get_requirements():
    course_hashmap = { "Computer Science" : "https://www.undergraduate.study.cam.ac.uk/courses/computer-science", 
    "Chemical Engineering" : "https://www.undergraduate.study.cam.ac.uk/courses/chemical-engineering",
    "Mathematics" : "https://www.undergraduate.study.cam.ac.uk/courses/mathematics"
    }
    input_course = "Mathematics"
    return requirements(course_hashmap.get(input_course))

get_requirements()
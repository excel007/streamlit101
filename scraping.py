import requests
from bs4 import BeautifulSoup


req = requests.get('https://stackpython.co/courses')

req.encoding = "utf-8"
# Create a BeautifulSoup object
soup = BeautifulSoup(req.text,'html.parser')
courses = soup.find_all('h2')
# print(courses)

course_list = []
for course in courses:
    course_list.append(course.string)
# print(soup.prettify())

import csv
# csv_col = [["column names"],["data or value"]]
csv_col = [["column names"],[course_list]]
f = open('web.csv','w')
with f:
    writer = csv.writer(f)
    for row in csv_col:
        writer.writerow(row)

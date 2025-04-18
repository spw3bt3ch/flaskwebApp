from re import template
from flask import Flask, render_template

courses = [{}]

app = Flask(__name__, template_folder='templates')

other_courses = [{
    "id":
    1,
    "name":
    "Python",
    "description":
    "Python is a high-level, interpreted programming language.",
    "price":
    100,
    "image":
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
}, {
    "id":
    2,
    "name":
    "Java",
    "description":
    "Java is a high-level, interpreted programming language.",
    "price":
    100,
    "image":
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
}, {
    "id":
    3,
    "name":
    "C++",
    "description":
    "C++ is a high-level, interpreted programming language.",
    "price":
    100,
    "image":
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
}, {
    "id":
    4,
    "name":
    "C#",
    "description":
    "C# is a high-level, interpreted programming language.",
    "price":
    100,
    "image":
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
}, {
    "id": 5,
    "name": "Ruby",
    "description": "Ruby is a high-level, interpreted programming language.",
    "price": 100,
}]


@app.route('/')
def index():
  return render_template('home.html', programming_courses=other_courses)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)

from flask import Flask, render_template
from datetime import datetime
import requests
app =Flask(__name__)

@app.route('/')
def runApp():
    currentyear = datetime.now().strftime("%Y")
    return 'Hello World'

def get_the_gender(given_name):
    genderizeAPI = 'https://api.genderize.io'
    param = {
        'name': given_name
    }
    response = requests.get(genderizeAPI, params=param).json()
    return response['gender']

def get_the_age(given_name):
    agifyAPI = 'https://api.agify.io'
    param = {
        'name': given_name
    }
    response = requests.get(agifyAPI, params=param).json()
    return response['age']

@app.route('/guess/<name>')
def guess_name(name):
    guessgender = get_the_gender(name)
    guessage = get_the_age(name)
    return render_template('index.html', name=name.title(), gender=guessgender.title(), age=guessage)

@app.route('/blog')
def blog_site():
    blogs = requests.get('https://api.npoint.io/70b9bd1a90bbe8eeccf5').json()
    return render_template('blog.html', blog_data=blogs)

if __name__ == '__main__':
    app.run(debug=True)
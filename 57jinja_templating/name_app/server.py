# https://flask.palletsprojects.com/en/1.1.x/quickstart/
from flask import Flask, render_template
from apis import GuessName
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1> My App.</h1>'
   

@app.route('/guess')
def guess():
    return  '<h1> Hi, enter a name in the URL and we will return the likely gender and average age of the name.</h1>'

@app.route('/guess/<name>')
def show_gender_age(name):
    name = name.title()
    guess = GuessName(name)
    gender = guess.get_gender()
    age = guess.get_age()
    return render_template("index.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)




# then set up an @app.route with <variable> the name
# then set up request to get the gender and then the agify
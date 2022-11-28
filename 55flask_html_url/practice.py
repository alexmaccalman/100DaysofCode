# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run()
    #app.run(debug=True)

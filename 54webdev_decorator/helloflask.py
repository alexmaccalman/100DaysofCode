# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)




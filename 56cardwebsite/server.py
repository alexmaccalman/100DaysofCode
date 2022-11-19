# https://flask.palletsprojects.com/en/1.1.x/quickstart/

# to get a free template go to https://html5up.net/  and download one. 
# in Chrome - open up Chrome developer tools, go to Console, and type some javascript - document.body.contentEditable=true
# after editing the html, save as to get teh html code locally. 
# to get great images for background use unsplash.com

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    #app.run()
    app.run(debug=True)




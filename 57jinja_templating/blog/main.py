from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_posts = response.json()
# make a list of objects
post_objects = []
for post in all_posts:
    # append each Post object declaration
    post_objects.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))



app = Flask(__name__)

@app.route('/')
def get_blog():
    return render_template("index.html", posts=post_objects)

@app.route("/post/<int:num>")
def get_post(num):
    # loop through the posts to find the one that is passed in with num
    requested_post = None
    for post in post_objects:  
        if post.id == num:
            requested_post = post
            print(requested_post.id)
    # render with the post object, the post variable is what will be used inside the post.html file
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

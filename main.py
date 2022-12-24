from flask import Flask,render_template
import requests


app =Flask(__name__)

posts=requests.get("https://mocki.io/v1/498158dd-1f37-4c2a-9501-b356add4f4f5").json()



@app.route("/")
def home():
    return render_template("index.html",all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blogs/<int:index>")
def get_post(index):

    return render_template("post.html",id=index,all_posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
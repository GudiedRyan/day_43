from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_num = random.randint(1,10)
    now = dt.datetime.now()
    year = now.year
    return render_template("index.html", random_num=random_num, year=year)


@app.route('/guess/<string:name>')
def guess(name):
    response = requests.get(url=f'https://api.agify.io?name={name}')
    age = response.json()["age"]
    response = requests.get(url=f'https://api.genderize.io?name={name}')
    gender = response.json()["gender"]
    return render_template('guess.html', name=name, age=age, gender=gender)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/b35ed8fac43ef21e0945"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

@app.route('/blog/<int:id>')
def read_blog(id):
    blog_url = "https://api.npoint.io/b35ed8fac43ef21e0945"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    blog_post = None
    for blog in all_posts:
        if blog["id"] == id:
            blog_post = blog
    return render_template("single_blog.html", blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)
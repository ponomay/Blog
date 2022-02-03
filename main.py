from flask import Flask, render_template
import requests


app = Flask(__name__)
n_point = "https://api.npoint.io/23926e6d17cdf434e8ba"
response = requests.get(n_point).json()

@app.route('/')
def home():

    return render_template("index.html", blogs=response)


@app.route('/about.html')
def about_page():
    return render_template("about.html")


@app.route('/contact.html')
def contact_page():
    return render_template("contact.html")


@app.route('/post.html/<post_id>')
def post_post(post_id):
    return render_template("post.html", post=(int(post_id) - 1), blogs=response)



if __name__ == "__main__":
    app.run(debug=True)

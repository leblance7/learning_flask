## Importing flask from Flask application.
from flask import Flask, render_template, url_for

## Setting the name name for the flask application.
app = Flask(__name__)

## Setting the website address for the website
@app.route('/')

def index():
## Opening localhost:5000 is the developement browser.
        return render_template("index.html")

if __name__ == "__main__":
        app.run(debug = "True")

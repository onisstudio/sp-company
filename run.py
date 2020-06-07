import os, json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/characters')
def characters():
    data = []
    with open("data/characters.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("characters.html", page_title="Characters", characters=data)

@app.route('/about')
def about():
    return render_template("about.html", page_title="About")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
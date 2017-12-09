import os
import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
#from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# from models import Result

@app.route('/proximo_domingo')
def proximo_domingo():
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    print('blabla')
    if request.method == "POST":
        # get url that the user has entered
        try:
            url = request.form['url']
            print(url, 'blabla')
            r = requests.get(url)
            print(r.text)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return render_template('index.html', errors=errors, results=results)
        raw = BeautifulSoup(r.text, 'html.parser').get_text()
        return render_template('index.html', errors=[raw], results=raw)
    return render_template('index.html', errors=errors, results=results)



if __name__ == '__main__':
    app.run()

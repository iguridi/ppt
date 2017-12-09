import os
import requests
from flask import Flask, render_template, request, send_from_directory, current_app
from bs4 import BeautifulSoup
#from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
#app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# from models import Result

@app.route('/next_sunday')
def next_sunday():

    from maker import scrapper, pptMaker
    folder = '/maker'
    directory = os.path.dirname(__file__)
    BASE_PPT = directory + folder + '/plantilla python.pptx'
    OUTPUT_PPT = directory + folder + '/ppt_listo.pptx'
    SLIDE_SIZE = 730
    PPT_TITLE = 'hooola'
    ADDRS = scrapper.ADDRS
    READINGS = scrapper.READINGS
    DATE = scrapper.FECHA
    pptMaker.Maker(READINGS, BASE_PPT, OUTPUT_PPT, SLIDE_SIZE, ADDRS, DATE, PPT_TITLE)
    # from maker import __init__
    # full path:
    # path = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    print('hooola')
    path = current_app.root_path + folder
    print(path)
    return send_from_directory(directory=path, filename='ppt_listo.pptx')



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

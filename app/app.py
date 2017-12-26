import os
import sys
import requests
from flask import Flask, render_template, request, send_from_directory, current_app
from bs4 import BeautifulSoup


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/download-ppt', methods=['GET', 'POST'])
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
<<<<<<< HEAD
<<<<<<< HEAD
    if request.method == "POST":
        print(request.form)

    # DATE = scrapper.FECHA
=======
    DATE = scrapper.FECHA

    if request.method == "POST":
        print(request.form)

>>>>>>> Changed requests
=======
    DATE = scrapper.FECHA

    if request.method == "POST":
        print(request.form)

>>>>>>> a1335a1b2e96ce19034f1c95dc576cd8c469a2da
    pptMaker.Maker(READINGS, BASE_PPT, OUTPUT_PPT, SLIDE_SIZE, ADDRS, DATE, PPT_TITLE)

    path = current_app.root_path + folder
    return send_from_directory(directory=path, filename='ppt_listo.pptx',
        as_attachment=True, attachment_filename=DATE + '.pptx')



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

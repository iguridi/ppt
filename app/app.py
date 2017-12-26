import os
import sys
import datetime
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
    if request.method == "POST":

        PPT_TITLE = request.form['title']
        date = request.form['date']
        #Convert date to datetime object
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        url = make_url(date)
        date = str(date.day) + ' ' + monthName(date.month) + ' ' + str(date.year)
        ADDRS, READINGS= scrapper.run(url)


    pptMaker.Maker(READINGS, BASE_PPT, OUTPUT_PPT, SLIDE_SIZE, ADDRS, date, PPT_TITLE)
    path = current_app.root_path + folder
    return send_from_directory(directory=path, filename='ppt_listo.pptx',
        as_attachment=True, attachment_filename=date + '.pptx')


def make_url(date):
    BASE_URL = 'http://www.eucaristiadiaria.cl/'
    if date.weekday() == 0:
        url = BASE_URL + 'domingo.php'
    else:
        url = BASE_URL + 'dia_cal.php?fecha=' + str(date)
    return url


def monthName(month_number):
    months = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
    return months[month_number]



@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    results = {}
    return render_template('index.html', errors=errors, results=results)



if __name__ == '__main__':
    app.run()

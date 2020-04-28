import os
import sys
import datetime
from datetime import datetime
# #HTTP error handling:
# import werkzeug
# Web Scrapping:
import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, send_from_directory, current_app

flask_app = Flask(__name__)
# app.config.from_object('config')
flask_app.config['DEBUG'] = True

BASE_URL = 'http://www.eucaristiadiaria.cl/'

BASE_PPT = 'plantilla-tema-oscuro.pptx'
OUTPUT_PPT = 'ppt_listo.pptx'


@flask_app.route('/download-ppt', methods=['GET', 'POST'])
def download():
    from maker import scrapper, ppt_maker
    folder = 'maker'
    directory = os.path.dirname(__file__)
    base_ppt = os.path.join(directory, folder, BASE_PPT)
    output_ppt = os.path.join(directory, folder, OUTPUT_PPT)

    title = request.args['title']
    date = request.args['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    url = make_url(date)

    date = ' '.join([str(date.day), month_name(date.month), str(date.year)])
    addrs, readings = scrapper.run(url)

    ppt_maker.Maker(base_ppt, output_ppt, addrs, readings, title, date)

    path = os.path.join(current_app.root_path, folder)

    return send_from_directory(directory=path,
                               filename=OUTPUT_PPT,
                               as_attachment=True,
                               attachment_filename=date + '.pptx')


def make_url(date):
    BASE_URL = 'http://www.eucaristiadiaria.cl/'
    if date.weekday() == 6:
        url = BASE_URL + 'domingo.php'
    else:
        url = BASE_URL + 'dia_cal.php?fecha=' + str(date)
    return url


def month_name(month_number):
    months = [
        "", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
        "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    return months[month_number]


flask_app.register_error_handler(500, lambda e: 'bad request!')


@flask_app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index2.html')


if __name__ == '__main__':
    flask_app.run()

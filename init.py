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

from scrapper import scrapper
from app import ppt_maker

flask_app = Flask(__name__)

BASE_URL = "http://www.eucaristiadiaria.cl/"
BASE_PPT = "ppt_templates/plantilla-youtube.pptx"
OUTPUT_PPT = "ppt_templates/ppt_listo.pptx"
BASE_URL = "http://www.eucaristiadiaria.cl/"


@flask_app.route("/download-ppt", methods=["GET", "POST"])
def download():
    FOLDER = "app"
    directory = os.path.dirname(__file__)
    base_ppt = os.path.join(directory, FOLDER, BASE_PPT)
    output_ppt = os.path.join(directory, FOLDER, OUTPUT_PPT)

    title = request.args["title"]
    date = request.args["date"]
    date = datetime.strptime(date, "%Y-%m-%d")
    url = f"{BASE_URL}dia_cal.php?fecha={date}"
    date_formatted = f"{date.day} {month_name(date.month)} {date.year}"
    addrs, readings = scrapper.run(url)

    ppt_maker.Maker(base_ppt, output_ppt, addrs, readings, title, date_formatted)

    path = os.path.join(current_app.root_path, FOLDER)

    return send_from_directory(
        directory=path,
        path=OUTPUT_PPT,
        as_attachment=True,
        attachment_filename=date_formatted + ".pptx",
    )


def month_name(month_number):
    months = [
        "",
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]
    return months[month_number]


def handle_error(e):
    print("Error:", e)
    return "Hubo un problema con esta solicitud"


flask_app.register_error_handler(500, handle_error)


@flask_app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


debug = os.environ.get("FLASK_ENV") == "development"
if __name__ == "__main__":
    flask_app.run(debug=debug)

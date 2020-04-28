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

from maker import scrapper, ppt_maker

flask_app = Flask(__name__)
flask_app.config["DEBUG"] = True

BASE_URL = "http://www.eucaristiadiaria.cl/"

BASE_PPT = "plantilla-youtube.pptx"
OUTPUT_PPT = "ppt_listo.pptx"
BASE_URL = "http://www.eucaristiadiaria.cl/"


@flask_app.route("/download-ppt", methods=["GET", "POST"])
def download():
    folder = "maker"
    directory = os.path.dirname(__file__)
    base_ppt = os.path.join(directory, folder, BASE_PPT)
    output_ppt = os.path.join(directory, folder, OUTPUT_PPT)

    title = request.args["title"]
    date = request.args["date"]
    date = datetime.strptime(date, "%Y-%m-%d")
    url = f"{BASE_URL}dia_cal.php?fecha={date}"
    date_formatted = f"{date.day} {month_name(date.month)} {date.year}"
    addrs, readings = scrapper.run(url)

    ppt_maker.Maker(base_ppt, output_ppt, addrs, readings, title, date_formatted)

    path = os.path.join(current_app.root_path, folder)

    return send_from_directory(
        directory=path,
        filename=OUTPUT_PPT,
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


flask_app.register_error_handler(500, lambda e: "bad request!")


@flask_app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index2.html")


if __name__ == "__main__":
    flask_app.run()

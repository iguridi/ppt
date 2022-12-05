# from io import StringIO
import io
import os
import sys
import datetime
from datetime import datetime

# #HTTP error handling:
# import werkzeug
# Web Scrapping:
import requests
import tempfile
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, send_file, current_app

from scrapper import scrapper
from app import ppt_maker

app = Flask(__name__)

BASE_URL = "https://www.eucaristiadiaria.cl/"
BASE_PPT = "ppt_templates/plantilla python.pptx"
OUTPUT_PPT = "ppt_listo2.pptx"


@app.route("/download-ppt", methods=["GET", "POST"])
def download():
    FOLDER = "app"
    base_ppt = os.path.join(os.path.dirname(__file__), FOLDER, BASE_PPT)

    title = request.args["title"]
    date = request.args["date"]
    date = datetime.strptime(date, "%Y-%m-%d")
    url = f"{BASE_URL}dia_cal.php?fecha={date}"
    date_formatted = f"{date.day} {month_name(date.month)} {date.year}"
    addrs, readings = scrapper.run(url)

    if addrs == {} and readings == {}:
        return f'''Fecha {date_formatted} vacía.
        <br/><br/>Probablemente signifique que ese día no ha sido llenado aún en
        <a href="https://www.eucaristiadiaria.cl/calendario.php">https://www.eucaristiadiaria.cl</a>.
        <br/><br/>Por mientras se pueden descargar fechas anteriores a esta desde la
        <a href="/">página principal</a>
        '''

    output = ppt_maker.Maker(base_ppt, addrs, readings, title, date_formatted).run()

    return send_file(
        output,
        as_attachment=True,
        download_name=date_formatted + ".pptx",
        mimetype="application/vnd.openxmlformats-officedocument.presentationml.presentation",
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


app.register_error_handler(500, handle_error)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


debug = os.environ.get("FLASK_ENV") == "development"
if __name__ == "__main__":
    app.run(debug=debug)

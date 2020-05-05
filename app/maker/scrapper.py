import re
import os
import json
from bs4 import BeautifulSoup
import requests
import logging


class ReadingFormatter:
    def __init__(self):
        self.books = self.get_books()

    def format_reading(self, text, reading):
        for book in self.books:
            book_name = book["name"]
            res = re.search(fr"{book_name}.*?(\d?\d,[-\.\d\s]*\d)\n([\s\S]+)\n", text)
            if res is not None:
                number = ""
                if "Corint" in book["name"]:
                    if "Lectura de la primera" in text:
                        number = "1 "
                    if "Lectura de la segunda" in text:
                        number = "2 "
                address = f"{number}{book['abbrs'][0]} {res.group(1)}"
                reading = res.group(2)
                reading = reading.replace("\n", " ")
                reading = reading.replace("  ", " ")
                return address, reading
        logging.error(f"'{reading} couldn't be formatted '{text}'")
        return None, None

    def get_books(self):
        abreviations_file = "abbreviations.csv"
        path = os.path.join(os.path.dirname(__file__), abreviations_file)
        with open(path) as f:
            rows = f.read().split("\n")
            data = (row.split(",") for row in rows[1:])
            books = [{"name": row[0], "abbrs": row[1:]} for row in data]
        return books


reading_formatter = ReadingFormatter()


def format_salm(text, reading):
    res = re.search(r"(\d?\d,[-\.\d\s]*\d)\.?\nR/.([\s\S]+)", text)
    address = "Sal " + res.group(1) if res else None
    salm = None
    if res is not None:
        salm = res.group(2)
        salm = salm.replace(".\n", ". R. ")
        salm = salm.replace("!\n", "! R. ")
        salm = salm.replace("\n", "")
        salm = salm.replace("  ", " ")
    else:
        logging.error(f"'{reading} couldn't be formatted '{text}'")
    return address, salm


def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    content = soup.find("div", class_="cuadro_interior")
    return content.text


def get_readings(text):
    parts = {}

    def add_to_dict(key, regex):
        res = re.search(regex, text)
        if res:
            parts[key] = res.group(1)

    add_to_dict("first_reading", r"PRIMERA LECTURA([\s\S]+?)SALMO")
    add_to_dict("salm", r"RESPONSORIAL([\s\S]+?)(SEGUNDA LECTURA|EVANGELIO)")
    add_to_dict("second_reading", r"SEGUNDA LECTURA([\s\S]+?)EVANGELIO")
    add_to_dict("gospel", r"EVANGELIO([\s\S]+?)(Credo.|LITURGIA EUCARÍSTICA)")
    # Adding a ? on a quantifier (?, * or +) makes it non-greedy
    # [\s\S] matches anything (\s: space, \S: non-space)
    # res = re.search(r"PRIMERA LECTURA([\s\S]+?)SALMO", text)
    # if res:
    #     parts["first_reading"] = res.group(1)

    # res = re.search(r"RESPONSORIAL([\s\S]+?)(SEGUNDA LECTURA|EVANGELIO)", text)
    # if res:
    #     parts["salm"] = res.group(1)

    # res = re.search(r"SEGUNDA LECTURA([\s\S]+?)EVANGELIO", text)
    # if res:
    #     parts["second_reading"] = res.group(1)

    # res = re.search(r"EVANGELIO([\s\S]+?)(Credo.|LITURGIA EUCARÍSTICA)", text,)
    # if res:
    #     parts["gospel"] = res.group(1)
    return parts


def run(url):
    text = get_text(url)

    addrs, readings = {}, {}

    readings_raw = get_readings(text)

    mapping_spn = {
        "first_reading": "primera_lectura",
        "salm": "salmo",
        "second_reading": "segunda_lectura",
        "gospel": "evangelio",
    }

    mapping_fnc = {
        "first_reading": reading_formatter.format_reading,
        "salm": format_salm,
        "second_reading": reading_formatter.format_reading,
        "gospel": reading_formatter.format_reading,
    }

    for key in readings_raw:
        spanish = mapping_spn[key]
        function = mapping_fnc[key]
        addrs[spanish], readings[spanish] = function(readings_raw[key], key)

    return addrs, readings


if __name__ == "__main__":
    url = "http://www.eucaristiadiaria.cl/dia_cal.php?fecha=2020-05-10"
    url = "http://www.eucaristiadiaria.cl/dia_cal.php?fecha=2020-05-06"
    res = run(url)
    print(json.dumps(res, indent=4))

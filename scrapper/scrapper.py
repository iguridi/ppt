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
            res = re.search(fr"{book_name}.*?(\d.*)\n([\s\S]+)\n", text)
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
                reading = reading.rstrip()
                return address, reading
        logging.error(f'"Bible book not recognized for {reading}: "{text}"')
        return None, None

    def get_books(self):
        abreviations_file = "abbreviations.csv"
        path = os.path.join(os.path.dirname(__file__), abreviations_file)
        with open(path) as f:
            rows = f.read().split("\n")[:-1]
            data = (row.split(",") for row in rows[1:])
            books = [{"name": row[0], "abbrs": row[1:]} for row in data]
        return books


reading_formatter = ReadingFormatter()


def format_salm(text, reading):
    res = re.search(r"(\d.*?)\.?\n([\s\S]+)", text)
    address = "Sal " + res.group(1) if res else None
    salm = None
    if res is not None:
        salm = res.group(2)
        salm = salm.replace(".\n", ". R. ")
        salm = salm.replace("!\n", "! R. ")
        salm = salm.replace("\n", "")
        salm = salm.replace("  ", " ")
        salm = salm.rstrip()
    else:
        err = {"text": text}
        logging.error(f'"{reading} (salm) couldn\'t be formatted: "{err}"')
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

    # Adding a ? on a quantifier (?, * or +) makes it non-greedy
    # [\s\S] matches anything (\s: space, \S: non-space)
    add_to_dict("first_reading", r"LITURGIA DE LA PALABRA([\s\S]+?)SALMO")
    add_to_dict("salm", r"RESPONSORIAL([\s\S]+?)(SEGUNDA LECTURA|EVANGELIO)")
    add_to_dict("second_reading", r"SEGUNDA LECTURA([\s\S]+?)(SECUENCIA|EVANGELIO)")
    add_to_dict("gospel", r"EVANGELIO([\s\S]+?)(Credo.|LITURGIA EUCARÍSTICA)")
    return parts


def run(url):
    text = get_text(url)

    addrs, readings = {}, {}

    readings_raw = get_readings(text)

    mapping_fnc = {
        "first_reading": reading_formatter.format_reading,
        "salm": format_salm,
        "second_reading": reading_formatter.format_reading,
        "gospel": reading_formatter.format_reading,
    }

    for key in readings_raw:
        function = mapping_fnc[key]
        addrs[key], readings[key] = function(readings_raw[key], key)

    return addrs, readings


if __name__ == "__main__":
    url = "https://www.eucaristiadiaria.cl/dia_cal.php?fecha=2023-6-08"
    res = run(url)
    print(json.dumps(res, indent=4))

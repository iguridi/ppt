from . import scrapper

from pytest import mark


def test_get_readings_sunday():
    url = "http://www.eucaristiadiaria.cl/dia_cal.php?fecha=2020-05-10"
    text = scrapper.get_text(url)
    readings = scrapper.get_readings(text)
    assert readings["first_reading"] != ""
    assert readings["salm"] != ""
    assert readings["second_reading"] != ""
    assert readings["gospel"] != ""


def test_get_readings_not_sunday():
    url = "http://www.eucaristiadiaria.cl/dia_cal.php?fecha=2020-05-06"
    text = scrapper.get_text(url)
    readings = scrapper.get_readings(text)
    assert readings["first_reading"] != ""
    assert readings["salm"] != ""
    assert "second_reading" not in readings
    assert readings["gospel"] != ""


def test_get_books():
    books = scrapper.reading_formatter.get_books()
    assert isinstance(books[0]["name"], str)
    assert isinstance(books[0]["abbrs"], list)


@mark.parametrize(
    "text,address,reading",
    [
        (
            "\nEligieron a siete hombres llenos del Espíritu Santo.\nLectura de los Hechos de los Apóstoles\xa0 6, 1-7\nEn aquellos días:\nComo el número de discípulos aumentaba, los helenistas comenzaron a murmurar contra los hebreos porque se desatendía a sus viudas en la distribución diaria de los alimentos.\nAsí la Palabra de Dios se extendía cada vez más, el número de discípulos aumentaba considerablemente en Jerusalén y muchos sacerdotes abrazaban la fe.\n",
            "Hch 6, 1-7",
            "En aquellos días: Como el número de discípulos aumentaba, los helenistas comenzaron a murmurar contra los hebreos porque se desatendía a sus viudas en la distribución diaria de los alimentos. Así la Palabra de Dios se extendía cada vez más, el número de discípulos aumentaba considerablemente en Jerusalén y muchos sacerdotes abrazaban la fe.",
        ),
        (
            "\nEl Señor se apareció a Santiago y a todos los apóstoles.\nLectura de la primera carta del Apóstol san Pablo a los cristianos de Corinto 15, 1-8\nHermanos:\nLes recuerdo la Buena Noticia que yo les he predicado, que ustedes han recibido y a la cual permanecen fieles. [...] Por último, se me apareció también a mí, que soy como el fruto de un aborto.\n",
            "1 Co 15, 1-8",
            "Hermanos: Les recuerdo la Buena Noticia que yo les he predicado, que ustedes han recibido y a la cual permanecen fieles. [...] Por último, se me apareció también a mí, que soy como el fruto de un aborto.",
        ),
        (
            "\nEl Señor se apareció a Santiago y a todos los apóstoles.\nLectura de la segunda carta del Apóstol san Pablo a los cristianos de Corinto 15, 1-8\nHermanos:\nLes recuerdo la Buena Noticia que yo les he predicado, que ustedes han recibido y a la cual permanecen fieles. [...] Por último, se me apareció también a mí, que soy como el fruto de un aborto.\n",
            "2 Co 15, 1-8",
            "Hermanos: Les recuerdo la Buena Noticia que yo les he predicado, que ustedes han recibido y a la cual permanecen fieles. [...] Por último, se me apareció también a mí, que soy como el fruto de un aborto.",
        ),
        (
            "\nEl Señor se apareció a Santiago y a todos los apóstoles.\nLectura de la segunda carta del Apóstol san Pablo a los cristianos de Corinto 15, 1-8. 6\nHermanos:\nLes recuerdo la Buena Noticia que yo les he predicado, que ustedes han recibido y a la cual permanecen fieles. [...] Por último, se me apareció también a mí, que soy como el fruto de un aborto.\n",
            "2 Co 15, 1-8. 6",
            "Hermanos: Les recuerdo la Buena Noticia que yo les he predicado, que ustedes han recibido y a la cual permanecen fieles. [...] Por último, se me apareció también a mí, que soy como el fruto de un aborto.",
        ),
    ],
)
def test_format_first_reading(text, address, reading):
    address1, reading1 = scrapper.reading_formatter.format_reading(text, "dummy")
    assert address == address1
    assert reading == reading1


@mark.parametrize(
    "text, address, reading",
    [
        (
            "\xa0\xa0 32, 1-2. 4-5. 19\nR/. Señor, que descienda tu amor sobre nosotros.\nAclamen, justos, al Señor: es propio de los buenos alabarlo. Alaben al Señor con la cítara, toquen en su honor el arpa de diez cuerdas.\nPorque la palabra del Señor es recta y Él obra siempre con lealtad; Él ama la justicia y el derecho, y la tierra está llena de su amor.\nLos ojos del Señor están fijos sobre sus fieles, sobre los que esperan en su misericordia, para librar sus vidas de la muerte y sustentarlos en el tiempo de indigencia.\n",
            "Sal 32, 1-2. 4-5. 19",
            "Señor, que descienda tu amor sobre nosotros. R. Aclamen, justos, al Señor: es propio de los buenos alabarlo. Alaben al Señor con la cítara, toquen en su honor el arpa de diez cuerdas. R. Porque la palabra del Señor es recta y Él obra siempre con lealtad; Él ama la justicia y el derecho, y la tierra está llena de su amor. R. Los ojos del Señor están fijos sobre sus fieles, sobre los que esperan en su misericordia, para librar sus vidas de la muerte y sustentarlos en el tiempo de indigencia. R. ",
        ),
        (
            ". Sal. 18, 2-5.\nR/. Resuena su eco por toda la tierra.\nEl cielo proclama la gloria de Dios y el firmamento anuncia la obra de sus manos; un día transmite al otro este mensaje y las noches se van dando la noticia.\nSin hablar, sin pronunciar palabras, sin que se escuche su voz, resuena su eco por toda la tierra y su lenguaje, hasta los confines del mundo.\n\n",
            "Sal 18, 2-5",
            "Resuena su eco por toda la tierra. R. El cielo proclama la gloria de Dios y el firmamento anuncia la obra de sus manos; un día transmite al otro este mensaje y las noches se van dando la noticia. R. Sin hablar, sin pronunciar palabras, sin que se escuche su voz, resuena su eco por toda la tierra y su lenguaje, hasta los confines del mundo. R. ",
        ),
    ],
)
def test_format_salm(text, address, reading):
    address1, reading1 = scrapper.format_salm(text)
    assert address == address1
    assert reading == reading1

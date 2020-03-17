import sys

from ppt_maker import Maker
import scrapper

BASE_PPT = 'plantilla python.pptx'
OUTPUT_PPT = 'ppt_listo.pptx'

ADDRS = {}
READINGS = {}

PPT_TITLE = sys.argv[1]

#Data obtained from www.eucaristiadiaria.cl using scrapper.py

url = 'http://www.eucaristiadiaria.cl/domingo.php'
addrs, readings = scrapper.run(url)

DATE = 'fecha 1'


if __name__ == '__main__':
    Maker(BASE_PPT, OUTPUT_PPT, addrs, readings, PPT_TITLE, DATE)
import sys

from pptMaker import Maker
import scrapper

BASE_PPT = 'plantilla python.pptx'
END_PPT = 'ppt_listo.pptx'
SLIDE_SIZE = 730

ADDRS = {}
READINGS = {}

PPT_TITLE = sys.argv[1] #Change when running on server

#When extracts from the web
if len(sys.argv) > 2:
	#Data obtained from www.eucaristiadiaria.cl using scraper.py
	DATE = scrapper.FECHA

	#Bible readings addresses
	ADDRS['primera_lectura'] = scrapper.DIR_PRIMERA_LECTURA
	ADDRS['salmo'] = scrapper.DIR_SALMO
	ADDRS['segunda_lectura'] = scrapper.DIR_SEGUNDA_LECTURA
	ADDRS['evangelio'] = scrapper.DIR_EVANGELIO

	#Readings obtained from www.eucaristiadiaria.cl
	READINGS['primera_lectura'] = scrapper.PRIMERA_LECTURA
	READINGS['salmo'] = scrapper.SALMO
	READINGS['segunda_lectura'] = scrapper.SEGUNDA_LECTURA
	READINGS['evangelio'] = scrapper.EVANGELIO

else:
	with open("lecturas.txt", 'r', encoding = 'utf-8') as file:
		#Data obtained from a hardcoded text file

		DATE = iterar(file, "PRIMERA_LECTURA_DIR = ")

		ADDRS['primera_lectura'] = iterar(file, "SALMO_DIR = ")
		ADDRS['salmo'] = iterar(file, 'SEGUNDA_LECTURA_DIR = ')
		ADDRS['segunda_lectura'] = iterar(file, 'EVANGELIO_DIR = ')
		ADDRS['evangelio'] = iterar(file, 'PRIMERA_LECTURA')     

		READINGS['primera_lectura'] = iterar(file, "SALMO")
		READINGS['salmo'] = iterar(file, 'SEGUNDA_LECTURA')
		READINGS['segunda_lectura'] = iterar(file, 'EVANGELIO')
		READINGS['evangelio'] = iterar(file, 'SANTIAGO SCRAPPERS')


if __name__ == '__main__':
	Maker(READINGS, BASE_PPT, END_PPT, SLIDE_SIZE, ADDRS, DATE, PPT_TITLE)
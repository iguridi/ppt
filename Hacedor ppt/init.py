import sys

from pptMaker import Maker
import scrapper

BASE_PPT = 'plantilla python.pptx'
END_PPT = 'ppt_listo.pptx'
SLIDE_SIZE = 730

ADDRS = {}
LECTURES = {}

PPT_TITLE = sys.argv[1] #Change when running on server

#When extracts from the web
if len(sys.argv) > 2:
	DATE = scrapper.FECHA

	
	ADDRS['primera_lectura'] = scrapper.DIR_PRIMERA_LECTURA
	ADDRS['salmo'] = scrapper.DIR_SALMO
	ADDRS['segunda_lectura'] = scrapper.DIR_SEGUNDA_LECTURA
	ADDRS['evangelio'] = scrapper.DIR_EVANGELIO

	
	LECTURES['primera_lectura'] = scrapper.PRIMERA_LECTURA
	LECTURES['salmo'] = scrapper.SALMO
	LECTURES['segunda_lectura'] = scrapper.SEGUNDA_LECTURA
	LECTURES['evangelio'] = scrapper.EVANGELIO

else:
	with open("lecturas.txt", 'r', encoding = 'utf-8') as file:
		DATE = iterar(file, "PRIMERA_LECTURA_DIR = ")

		ADDRS['primera_lectura'] = iterar(file, "SALMO_DIR = ")
		ADDRS['salmo'] = iterar(file, 'SEGUNDA_LECTURA_DIR = ')
		ADDRS['segunda_lectura'] = iterar(file, 'EVANGELIO_DIR = ')
		ADDRS['evangelio'] = iterar(file, 'PRIMERA_LECTURA')     


		LECTURES['primera_lectura'] = iterar(file, "SALMO")
		LECTURES['salmo'] = iterar(file, 'SEGUNDA_LECTURA')
		LECTURES['segunda_lectura'] = iterar(file, 'EVANGELIO')
		LECTURES['evangelio'] = iterar(file, 'SANTIAGO SCRAPPERS')


if __name__ == '__main__':
	Maker(LECTURES, BASE_PPT, END_PPT, SLIDE_SIZE, ADDRS, DATE, PPT_TITLE)
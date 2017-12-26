import os
from bs4 import BeautifulSoup
import requests
import csv

class FirstReading:
	def __init__(self):
		self.text = ''

	def get_text(self):
		self.text


def get_page(url):
	PAGE = requests.get('http://www.eucaristiadiaria.cl/domingo.php')
	SOUP = BeautifulSoup(PAGE.content, 'html.parser')
	return PAGE, SOUP

def parse_date(raw_date):
	pass

def extract_all_text(SOUP):
	content = soup.find('div', class_= 'cuadro_interior')
	TEXT = content.find_all('div')
	return TEXT

# def find_readings():
# 	primera_lectura_name = 'Primera lectura'
# 	salmo_responsorial_name = 'Salmo responsorial'
# 	segunda_lectura_name = "Segunda Lectura"    
# 	credo_name = "Credo"

# 	def find_first_reading():
# 		pass
# 	def find_psalm():
# 		pass
# 	#If sunday:
# 		def find__second_reading():
# 			pass
# 	def find_gospel():
# 		pass

def make_books_dic():
	pass


def run(url, date):
	PAGE, SOUP = get_page(url)
	DATE, is_sunday = parse_date(date)
	if is_sunday:
		pass
	else:
		pass
	TEXT = extract_all_text(SOUP)
	READINGS = TEXT[8].get_text()




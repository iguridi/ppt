import os
from bs4 import BeautifulSoup
import requests
import csv

def remove_spaces(text):
	text = text.lstrip()
	text = text.rstrip()
	text = text.replace('  ', '')
	text = text.replace('  ', '')
	text = text.replace('  ', '')
	text = text.replace('  ', '')
	return text

def get_web_page(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	#Todo los textos de la pagina del Domingo
	contenido = soup.find('div', class_= 'cuadro_interior')
	text = contenido.find_all('div')
	return text


def crearListaLibros():
	#Crear la lista con diccionarios
	#En el csv van así: Nombre Completo, abreviacion, posible(otra abreviacion)
	abreviations_file = 'Abreviaciones Biblia.csv'
	path = os.path.join(os.path.dirname(__file__), abreviations_file)
	libros = []
	with open(path, 'r', encoding='utf-8') as abrv:
		bookReader = csv.DictReader(abrv)
		#Crear un diccionario
		for row in bookReader:
			row = {key: value for key, value in row.items() if value != ''}
			libros.append(row)

	return libros

def pulirDireccion(texto_general):
	libros = crearListaLibros()
	lbr = ''
	lbrAbrev = ''
	#Find the first word in the text that refers to a book name
	for palabra in texto_general.split(' '): #Buscar palabra por palabra
		palabra = palabra.strip() #Remove spaces
		for libro in libros: #Buscar un libro(en forma de diccionario) en la lista de libros
			if libro['Name'] == palabra:
				lbr = libro['Name']
				lbrAbrev = libro['Abreviattion'] #Replace the book name for its shortening
				break
		if lbrAbrev: break

	# Find the begining of the address
	book_pos = texto_general.find(lbr)

	last_number = ''
	# Find the ending of the address
	for last_number in texto_general[::-1]:
		if last_number.isdigit():
		   break
	#Por si un número se repite cuando se busca de left to rigth
	last_position = len(texto_general) - texto_general[::-1].find(last_number)
	#If the direcctions doesn't end in digits
	while True:
		if texto_general[last_position] == '\n':
			break
		last_position += 1
	direccion = texto_general[book_pos + len(lbr) : last_position]
	#Remove unnecesary spaces
	direccion = remove_spaces(direccion)
	return lbrAbrev + ' ' + direccion, last_position



def pulir(texto_general): # especifica la lecura.
	direccion, last_position = pulirDireccion(texto_general)
	texto = texto_general[last_position:]
	#Quitar espacios inecesarios
	texto = texto.strip()
	return direccion, texto

first_reading_name = 'Primera lectura'
salmo_responsorial_name = 'Salmo responsorial'
second_reading_name = "Segunda Lectura"
credo_name = "Credo"

def find_first_reading(text):
	rough_first_reading = text[text.find(first_reading_name):text.find(salmo_responsorial_name)]
	return rough_first_reading

def find_psalm(text):
	second_reading_name_pos = text.find(second_reading_name)
	rough_psalm = text[text.find(salmo_responsorial_name):second_reading_name_pos]
	#In case the day selected is an ordinary day.
	if second_reading_name_pos == -1:
		rough_psalm = text[text.find(salmo_responsorial_name):text.find('EVANGELIO')]
	rough_psalm = rough_psalm.replace(salmo_responsorial_name[5:], '')

	rough_psalm = rough_psalm.replace('.\n', '. R. ')		
	rough_psalm = rough_psalm.replace('!\n', '! R. ')
	# the psalm does not show when we have to answer
	i = rough_psalm.find(' R.')
	rough_psalm = rough_psalm[:i] + '***' + rough_psalm[i + 3:]

	return rough_psalm

def find_second_reading(text):
	try:
		text.index(second_reading_name)
	except ValueError:
		return
	rough_second_reading = text[text.find(second_reading_name)+15:text.find('SECUENCIA')]
	return rough_second_reading

def find_gospel(gospel_text):
	rough_gospel = gospel_text[gospel_text.find('Evangelio de nuestro Señor Jesucristo')+48:gospel_text.find(credo_name)-1]
	return rough_gospel


def find_readings(readings, gospel_text):
	rough_first_reading = find_first_reading(readings)
	rough_psalm = find_psalm(readings)
	rough_second_reading = find_second_reading(readings)
	rough_gospel = find_gospel(gospel_text)
	return (rough_first_reading, rough_psalm, rough_second_reading, rough_gospel)


def run(url):
	text = get_web_page(url)

	readings = str(text[8].text)
	gospel_text = str(text[10].text)

	rough_readings = find_readings(readings, gospel_text)
	if not rough_readings[0]:
		for n in [first_reading_name, salmo_responsorial_name, second_reading_name]:
			readings = readings.replace(n.upper(), n)
		rough_readings = find_readings(readings, gospel_text)

	rough_first_reading = rough_readings[0]
	rough_psalm = rough_readings[1]
	rough_second_reading = rough_readings[2]
	rough_gospel = rough_readings[3]

	dir_primera_lectura, primera_lectura = pulir(rough_first_reading)
	dir_salmo, salmo = pulir(rough_psalm)
	dir_evangelio, evangelio = pulir(rough_gospel)

	addrs = {}
	readings = {}

	if rough_second_reading:
		dir_segunda_lectura, segunda_lectura = pulir(rough_second_reading)
		addrs['segunda_lectura'] = dir_segunda_lectura
		readings['segunda_lectura'] = segunda_lectura

	addrs['primera_lectura'] = dir_primera_lectura
	addrs['salmo'] = dir_salmo
	addrs['evangelio'] = dir_evangelio
	
	readings['primera_lectura'] = primera_lectura
	readings['salmo'] = salmo
	readings['evangelio'] = evangelio

	return addrs, readings

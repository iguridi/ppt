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
	# finds the first word in the text that refers to a book
	for palabra in texto_general.split(' '): #Buscar palabra por palabra
		palabra = palabra.strip() #sacar espacios
		for libro in libros: #Buscar un libro(en forma de diccionario) an la lista de libros
			if libro['Name'] == palabra:
				lbr = libro['Name']
				lbrAbrev = libro['Abreviattion'] #Reemplazar el nombre del libro por su abreviacion
				break
		if lbrAbrev: break

	# Encontrar el principio de la direccion
	libroPosition = texto_general.find(lbr)

	ultimo_numero = ''
	#Encontrar el último número de la direccion
	for ultimo_numero in texto_general[::-1]:
		if ultimo_numero.isdigit():
		   break
	#Por si un número se repite cuando se busca de dr a izq
	last_position = len(texto_general) - texto_general[::-1].find(ultimo_numero)
	# for when de direcctions don't end in digits
	while True:
		if texto_general[last_position] == '\n':
			break
		last_position += 1


	direccion = texto_general[libroPosition + len(lbr) : last_position]
	#Quitar espacios inecesarios
	direccion = remove_spaces(direccion)
	return lbrAbrev + ' ' + direccion, last_position



def pulir(texto_general): # especifica la lecura.
	direccion, last_position = pulirDireccion(texto_general)
	texto = texto_general[last_position:]

	#Quitar espacios inecesarios
	texto = texto.lstrip()
	texto = texto.rstrip()
	return direccion, texto

primera_lectura_name = 'Primera lectura'
salmo_responsorial_name = 'Salmo responsorial'
segunda_lectura_name = "Segunda Lectura"
credo_name = "Credo"

def find_first_reading(text):
	rough_first_reading = text[text.find(primera_lectura_name):text.find(salmo_responsorial_name)]
	return rough_first_reading

def find_psalm(text):
	rough_psalm = text[text.find(salmo_responsorial_name):text.find(segunda_lectura_name)]
	rough_psalm = rough_psalm.replace(salmo_responsorial_name[5:], '')
	# the psalm does not show when we have to answer
	i = rough_psalm.find(' R.')
	rough_psalm = rough_psalm[:i] + '***' + rough_psalm[i + 3:]

	return rough_psalm

def find_second_reading(text):
	rough_second_reading = text[text.find(segunda_lectura_name)+15:text.find('SECUENCIA')]
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
	# URL = create_url(date)
	TEXT = get_web_page(url)

	readings = str(TEXT[8].text)
	gospel_text = str(TEXT[10].text)

	rough_readings = find_readings(readings, gospel_text)
	if not rough_readings[0]:
		for n in [primera_lectura_name, salmo_responsorial_name, segunda_lectura_name]:
			readings = readings.replace(n.upper(), n)
		rough_readings = find_readings(readings, gospel_text)

	rough_first_reading = rough_readings[0]
	rough_psalm = rough_readings[1]
	rough_second_reading = rough_readings[2]
	rough_gospel = rough_readings[3]

	DIR_PRIMERA_LECTURA, PRIMERA_LECTURA = pulir(rough_first_reading)
	DIR_SALMO, SALMO = pulir(rough_psalm)
	DIR_SEGUNDA_LECTURA, SEGUNDA_LECTURA = pulir(rough_second_reading)
	DIR_EVANGELIO, EVANGELIO = pulir(rough_gospel)


	ADDRS = {}
	ADDRS['primera_lectura'] = DIR_PRIMERA_LECTURA
	ADDRS['salmo'] = DIR_SALMO
	ADDRS['segunda_lectura'] = DIR_SEGUNDA_LECTURA
	ADDRS['evangelio'] = DIR_EVANGELIO

	READINGS = {}
	READINGS['primera_lectura'] = PRIMERA_LECTURA
	READINGS['salmo'] = SALMO
	READINGS['segunda_lectura'] = SEGUNDA_LECTURA
	READINGS['evangelio'] = EVANGELIO

	return ADDRS, READINGS

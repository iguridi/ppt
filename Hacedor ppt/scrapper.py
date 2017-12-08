'''
Copyright (c) 2017 Santiago Guridi. All rights reserved. 

 Redistribution and use in source and binary forms, with or without 
modification, arenn`t permitted without his permission
'''

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

page = requests.get('http://www.eucaristiadiaria.cl/domingo.php')
# page = requests.get('http://www.eucaristiadiaria.cl/dia_cal.php?fecha=2017-08-15')
soup = BeautifulSoup(page.content, 'html.parser')

contenido = soup.find('div', class_= 'cuadro_interior') #Todo los textos de la pagina del Domingo
texto = contenido.find_all('div')

lecturas = str(texto[8].text) #<div> que contiene las lecturas
#print(lecturas)
#FECHA
fecha = texto[0].text
print(fecha)
fecha = fecha[fecha.find("Domingo") + len("Domingo") : fecha.find("de 2") + len("de 2017")]
FECHA = fecha.replace("de ", "")
print("fecha:", FECHA)


	libroPosition = texto_general.find(lbr)


	#Encontrar el último número de la direccion
	for ultimo_numero in texto_general[::-1]: 
		if ultimo_numero.isdigit():
		   break
	last_position = len(texto_general) - texto_general[::-1].find(ultimo_numero) #Por si un número se repite cuando se busca de dr a izq   
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



#----------------------------------------------ACA PARTE TODO SOBRE LAS LECTURAS-----------------------------#

#(Los textos_generales son los con frases que no son de las lecturas mismas)

primera_lectura_name = 'Primera lectura'
salmo_responsorial_name = 'Salmo responsorial'
segunda_lectura_name = "Segunda Lectura"
creado_name = "Credo"


primera_lectura_general = lecturas[lecturas.find(primera_lectura_name):lecturas.find(salmo_responsorial_name)] 
if not primera_lectura_general:
	for i in [primera_lectura_name, salmo_responsorial_name, segunda_lectura_name]:
		lecturas = lecturas.replace(i.upper(), i)
	creado_name = creado_name.upper()
	print("Buscando lecturas con mayusculas activado")
	primera_lectura_general = lecturas[lecturas.find(primera_lectura_name):lecturas.find(salmo_responsorial_name)] 

salmo_general = lecturas[lecturas.find(salmo_responsorial_name):lecturas.find(segunda_lectura_name)]


salmo_general = salmo_general.replace(salmo_responsorial_name[5:], '')
# the salmo does not show when we have to answer

salmo_general = salmo_general.replace('.\n', '. R. ')
salmo_general = salmo_general.replace('!\n', '! R. ')


i = salmo_general.find(' R.')
salmo_general = salmo_general[:i] + '***' + salmo_general[i + 3:]


segunda_lectura_general = lecturas[lecturas.find(segunda_lectura_name)+15:lecturas.find('SECUENCIA')]

evangelio_div = str(texto[10].text) #Es otro <div>
evangelio_general = evangelio_div[evangelio_div.find('Evangelio de nuestro Señor Jesucristo')+48:evangelio_div.find(creado_name)-1]

DIR_PRIMERA_LECTURA, PRIMERA_LECTURA = pulir(primera_lectura_general)
DIR_SALMO, SALMO = pulir(salmo_general)
DIR_SEGUNDA_LECTURA, SEGUNDA_LECTURA = pulir(segunda_lectura_general)
DIR_EVANGELIO, EVANGELIO = pulir(evangelio_general)
def crearListaLibros():
	#En el csv van así: Nombre Completo, abreviacion, posible(otra abreviacion)
	libros = []
	with open('Abreviaciones Biblia.csv', 'r', encoding='utf-8') as abrv:
		bookReader = csv.DictReader(abrv)
		#Crear un diccionario
		for row in bookReader:
			row = {key: value for key, value in row.items() if value != ''}
			libros.append(row)

	return libros

def pulirDireccion(texto_general):
	libros = crearListaLibros() #Crear la lista con diccionarios
	lbr = ''
	lbrAbrev = ''
	# finds the first word in the text that refers to a book
	for palabra in texto_general.split(' '): #Buscar palabra por palabra
		palabra = palabra.strip() #sacar espacios
		for libro in libros: #Buscar un libro(en forma de diccionario) an la lista de libros
			print(palabra, libro['Name'])
			if libro['Name'] == palabra: 
				lbr = libro['Name']
				lbrAbrev = libro['Abreviattion'] #Reemplazar el nombre del libro por su abreviacion
				break
		if lbrAbrev: break


	#Encontrar el principio de la direccion



print(DIR_SALMO)






# -*- coding: utf-8 -*-

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


def crearListaLibros():
    #En el csv van así: Nombre Completo, abreviacion, posible(otra abreviacion)
    libros = []
    with open('Abreviaciones Biblia.csv', 'r', encoding='utf-8') as abrv:
        # csv_reader = csv.reader(abrv)
        # libros_no_dic = ([unicode(cell, 'utf-8') for cell in row 
        #                         if cell != '']
        #                     for row in csv_reader)
        # libros = [{'Abreviattion': row[1], 'Name': row[0]} for row in libros_no_dic]
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
    # finds the first word in the text taht refers to a book
    for palabra in texto_general.split(' '): #Buscar palabra por palabra
        palabra = palabra.lstrip() #sacar espacios
        palabra = palabra.rstrip() #sacar espacios
        for libro in libros: #Buscar un libro(en forma de diccionario) an la lista de libros
            if libro['Name'] == palabra: 
                lbr = libro['Name']
                lbrAbrev = libro['Abreviattion'] #Reemplazar el nombre del libro por su abreviacion
                break
        if lbrAbrev: break


    #Encontrar el principio de la direccion
    libroPosition = texto_general.find(lbr)


    #Encontrar el último número de la direccion
    for ultimo_numero in texto_general[::-1]: 
        if ultimo_numero.isdigit():
           break
    last_position = len(texto_general) - texto_general[::-1].find(ultimo_numero) #Por si un número se repite cuando se busca de dr a izq   
    # for when de direcctions don't end in digits
    while True:
        if texto_general[last_position] == '\n':
            # print(texto_general, last_position)
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

pl = 'Primera lectura'
sr = 'Salmo responsorial'
sl = "Segunda Lectura"
creado_name = "Credo"


primera_lectura_general = lecturas[lecturas.find(pl):lecturas.find(sr)] 
#direccion_primera_lectura, primera_lectura = pulir(primera_lectura_general)
if not primera_lectura_general:
    for i in [pl, sr, sl]:
        lecturas = lecturas.replace(i.upper(), i)
    creado_name = creado_name.upper()
    print("Buscando lecturas con mayusculas activado")
    primera_lectura_general = lecturas[lecturas.find(pl):lecturas.find(sr)] 

salmo_general = lecturas[lecturas.find(sr):lecturas.find(sl)]


salmo_general = salmo_general.replace(sl[5:], '')
# the salmo does not show when we have to answer

salmo_general = salmo_general.replace('.\n', '. R. ')
salmo_general = salmo_general.replace('!\n', '! R. ')
# salmo_general = salmo_general.replace('R/.', 'R. ')
# we put a mark where the answer finishes
# print(salmo_general, '\n')
print(repr(lecturas))
i = salmo_general.find(' R.')
salmo_general = salmo_general[:i] + 'santiago hizo esto' + salmo_general[i + 3:]

# print('ejeem', salmo_general)
#direccion_salmo, salmo = pulir(salmo_general)

segunda_lectura_general = lecturas[lecturas.find(sl)+15:lecturas.find('SECUENCIA')]
#direccion_segunda_lectura, segunda_lectura = pulir(segunda_lectura_general)

evangelio_div = str(texto[10].text) #Es otro <div>
print('evangelio', evangelio_div)
evangelio_general = evangelio_div[evangelio_div.find('Evangelio de nuestro Señor Jesucristo')+48:evangelio_div.find(creado_name)-1]
# direccion_evangelio, evangelio = pulir(evangelio)

DIR_PRIMERA_LECTURA, PRIMERA_LECTURA = pulir(primera_lectura_general)
DIR_SALMO, SALMO = pulir(salmo_general)
DIR_SEGUNDA_LECTURA, SEGUNDA_LECTURA = pulir(segunda_lectura_general)
DIR_EVANGELIO, EVANGELIO = pulir(evangelio_general)









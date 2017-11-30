from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.eucaristiadiaria.cl/domingo.php')
soup = BeautifulSoup(page.content, 'html.parser')

contenido = soup.find('div', class_= 'cuadro_interior') #Todo los textos de la pagina del Domingo
texto = contenido.find_all('div')
lecturas = str(texto[8].text) #<div> que contiene las lecturas 

def especificar(texto_general): #Encuentra la "direccion" de la lectura y la lectura misma.
    for capitulo in texto_general:
        if capitulo.isdigit():
            break
    for ultimo_numero in texto_general[::-1]:
        if ultimo_numero.isdigit():
            break

    position = len(texto_general) - texto_general[::-1].find(ultimo_numero) #Por si un número se repite cuando se busca de dr a izq
    direccion = texto_general[texto_general.find(capitulo) :position]
    texto = texto_general[texto_general.find(capitulo)+len(direccion):]

    return direccion, texto 

#Los textos_generales son los con frases que no son de las lecturas mismas

primera_lectura_general = lecturas[lecturas.find('Primera lectura'):lecturas.find('Salmo responsorial')] 
direccion_primera_lectura, primera_lectura = especificar(primera_lectura_general)

salmo_general = lecturas[lecturas.find('Salmo responsorial'):lecturas.find('Segunda lectura')]
direccion_salmo, salmo = especificar(salmo_general)

segunda_lectura_general = lecturas[lecturas.find('Segunda lectura')+15:lecturas.find('SECUENCIA')]
direccion_segunda_lectura, segunda_lectura = especificar(segunda_lectura_general)

evangelio_div = str(texto[10].text) #Es otro <div>
evangelio = evangelio_div[evangelio_div.find('Evangelio de nuestro Señor Jesucristo')+48:evangelio_div.find('Credo')-1]
# direccion_evangelio, evangelio = especificar(evangelio)

print(direccion_primera_lectura)
print(primera_lectura)
print(direccion_salmo)
print(salmo)
print(direccion_segunda_lectura)
print(segunda_lectura)
# print(direccion_evangelio)
print(evangelio)









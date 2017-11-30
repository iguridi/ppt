from bs4 import BeautifulSoup
import requests

page = requests.get('http://www.eucaristiadiaria.cl/domingo.php')
soup = BeautifulSoup(page.content, 'html.parser')
contenido = soup.find('div', class_= 'cuadro_interior')

texto = contenido.find_all('div')
#print(contenido)
lecturas = str(texto[8].text)
#lecturas = texto[8]
print(lecturas)
primera_lectura = lecturas[lecturas.find('Primera Lectura'):lecturas.find('Salmo')]
print(primera_lectura)
salmo = lecturas[lecturas.find('R/.'):lecturas.find('Segunda lectura')]
#print(salmo)
segunda_lectura = lecturas[lecturas.find('Segunda lectura')+15:lecturas.find('SECUENCIA')]
#print(segunda_lectura)

evangelio = str(texto[10].text)
evangelio = evangelio[:evangelio.find('Credo')-1]
#print(evangelio)

#for i in range(0, len(hola)):
#	print(i, hola[i])





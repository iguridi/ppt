# import requests
texto = \
'''    
Juan Bautista vio acercarse
a Jesús y dijo: “Éste es el
Cordero de Dios, que quita el 
pecado del mundo. A él me refería, cuando
dije: Después de mí viene un hombre que
me precede, porque existía antes que yo.
Yo no lo conocía, pero he venido a bautizar
con agua para que él fuera manifestado a
Israel”. Y Juan dio este testimonio: “He visto
al Espíritu descender del cielo en forma de
paloma y permanecer sobre él. Yo no lo
conocía, pero el que me envió a bautizar
con agua me dijo: “Aquél sobre el que veas
descender el Espíritu y permanecer sobre
él, ése es el que bautiza en el Espíritu
Santo”. Yo lo he visto y doy testimonio de
que él es el Hijo de Dios”
'''
texto = texto.replace('\n', ' ')
texto = texto.replace('  ', ' ')
texto = texto.replace('  ', ' ')
texto = texto.replace('  ', ' ')
texto = '    ' + texto



def separar_texto(texto):
	new_text = ''
	while len(texto) > 740:
		diap = texto[:740]
		i = len(diap) - diap[::-1].find('.')
		new_text +=  texto[:i] + '\n\n    '
		texto = texto[i:]
	return new_text + texto	

t = separar_texto(texto)
print(t)

print('Cantidad diapositivas: ', t.count('\n\n') + 1)

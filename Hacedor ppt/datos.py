# -*- coding: utf-8 -*-

from hacedor import *
import scrapper
import subprocess, os
import sys

# when de text is in a txt file
def iterar(file, hasta):
    lec = ''
    while True:
        a = file.read(1)
        if a == "": 
            print("finished")
            break
        lec += a
        if hasta in lec: 
            lec = lec[:-len(hasta)]
            break
    return lec 

office = r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"
ENC = 'utf-8'
PPT_BASE = 'plantilla.xml'
PPT_FINAL = 'ppt_listo.xml'
SLIDE_SIZE = 740

DIRS = {}
LECTURAS = {}

TITULO = sys.argv[1]

# when extracts from web
if len(sys.argv) > 20:
    FECHA = scrapper.FECHA

    
    DIRS['primera_lectura'] = scrapper.DIR_PRIMERA_LECTURA
    DIRS['salmo'] = scrapper.DIR_SALMO
    DIRS['segunda_lectura'] = scrapper.DIR_SEGUNDA_LECTURA
    DIRS['evangelio'] = scrapper.DIR_EVANGELIO

    
    LECTURAS['primera_lectura'] = scrapper.PRIMERA_LECTURA
    LECTURAS['salmo'] = scrapper.SALMO
    LECTURAS['segunda_lectura'] = scrapper.SEGUNDA_LECTURA
    LECTURAS['evangelio'] = scrapper.EVANGELIO  


else:
    with open("lecturas.txt", 'r', encoding = 'utf-8') as file:
        FECHA = iterar(file, "PRIMERA_LECTURA_DIR = ")

        DIRS['primera_lectura'] = iterar(file, "SALMO_DIR = ")
        DIRS['salmo'] = iterar(file, 'SEGUNDA_LECTURA_DIR = ')
        DIRS['segunda_lectura'] = iterar(file, 'EVANGELIO_DIR = ')
        DIRS['evangelio'] = iterar(file, 'PRIMERA_LECTURA')     


        LECTURAS['primera_lectura'] = iterar(file, "SALMO")
        LECTURAS['salmo'] = iterar(file, 'SEGUNDA_LECTURA')
        LECTURAS['segunda_lectura'] = iterar(file, 'EVANGELIO')
        LECTURAS['evangelio'] = iterar(file, 'SANTIAGO SCRAPPERS')     
    # DIRSDIRSDIRSDIRSDIRS = {'primera_lectura': " Ap 9a; 12, 1-6a. 10ab",#scrapper.DIR_PRIMERA_LECTURA,
#         'salmo': "Sal 44, 10b-12. 15b-16",#scrapper.DIR_SALMO,
#         'segunda_lectura': "Co 15, 20-27a", #scrapper.DIR_SEGUNDA_LECTURA,
#         'evangelio': "Lu  Lucas 11, 27-28",}#scrapper.DIR_EVANGELIO}
# LECTURAS = {
#     'primera_lectura' : #scrapper.PRIMERA_LECTURA,
# '''

# La Mujer tuvo un hijo varón que debía regir a todas las naciones con un cetro de hierro. Pero el hijo fue elevado hasta Dios y hasta su trono, y la Mujer huyó al desierto, donde Dios le había preparado un refugio.

# Y escuché una voz potente que resonó en el cielo:

# “Ya llegó la salvación, el poder y el Reino de nuestro Dios y la soberanía de su Mesías”.''',
#     'salmo' : #scrapper.SALMO,
# '''R. ¡De pie a tu derecha está la Reina, Señor! R

# Una hija de reyes está de pie a tu derecha: es la reina, adornada con tus joyas y con oro de Ofir. R.

# ¡Escucha, hija mía, mira y presta atención! Olvida tu pueblo y tu casa paterna, y el rey se prendará de tu hermosura. Él es tu señor: inclínate ante él. R.

# Las vírgenes van detrás, sus compañeras la guían, con gozo y alegría entran al palacio real. R.''',

#     'segunda_lectura' : #scrapper.SEGUNDA_LECTURA,
#     '''Hermanos:

# Cristo resucitó de entre los muertos, el primero de todos. Porque la muerte vino al mundo por medio de un hombre, y también por medio de un hombre viene la resurrección.

# En efecto, así como todos mueren en Adán, así también todos revivirán en Cristo, cada uno según el orden que le corresponde:

# Cristo, el primero de todos; luego, aquéllos que estén unidos a Él en el momento de su Venida.

# En seguida vendrá el fin, cuando Cristo entregue el Reino a Dios, el Padre, después de haber aniquilado todo Principado, Dominio y Poder. Porque es necesario que Cristo reine hasta que ponga a todos los enemigos debajo de sus pies. El último enemigo que será vencido es la muerte, ya que Dios “todo lo sometió bajo sus pies”.''',

#     'evangelio': #scrapper.EVANGELIO
#     '''HMaría partió y fue sin demora a un pueblo de la montaña de Judá. Entró en la casa de Zacarías y saludó a Isabel. Apenas ésta oyó el saludo de María, el niño saltó de alegría en su vientre, e Isabel, llena del Espíritu Santo, exclamó:

# “¡Tú eres bendita entre todas las mujeres y bendito es el fruto de tu vientre! ¿Quién soy yo, para que la madre de mi Señor venga a visitarme? Apenas oí tu saludo, el niño saltó de alegría en mi vientre. Feliz de ti por haber creído que se cumplirá lo que te fue anunciado de parte del Señor”.

# María dijo entonces:

# “Mi alma canta la grandeza del Señor, y mi espíritu se estremece de gozo en Dios, mi Salvador, porque Él miró con bondad la pequeñez de su servidora.

# En adelante todas las generaciones me llamarán feliz, porque el Todopoderoso ha hecho en mí grandes cosas: ¡su Nombre es santo!

# Su misericordia se extiende de generación en generación sobre aquéllos que lo temen.

# Desplegó la fuerza de su brazo, dispersó a los soberbios de corazón. Derribó a los poderosos de su trono y elevó a los humildes.

# Colmó de bienes a los hambrientos y despidió a los ricos con las manos vacías. Socorrió a Israel, su servidor, acordándose de su misericordia, como lo había prometido a nuestros padres, en favor de Abraham y de su descendencia para siempre”.

# María permaneció con Isabel unos tres meses y luego regresó a su casa.'''
# }


DIC = { 'portada':['<p:sldId id="256" r:id="rId2"/>'], 
        'primera_lectura':['<p:sldId id="257" r:id="rId3"/>', 
                        '<p:sldId id="264" r:id="rId4"/>', 
                        '<p:sldId id="265" r:id="rId5"/>',],
        'salmo':['<p:sldId id="258" r:id="rId6"/>'],
        'segunda_lectura':['<p:sldId id="259" r:id="rId7"/>',
                         '<p:sldId id="266" r:id="rId8"/>',
                         '<p:sldId id="267" r:id="rId9"/>',],
        'evangelio':['<p:sldId id="260" r:id="rId10"/>',
                     '<p:sldId id="268" r:id="rId11"/>',
                     '<p:sldId id="269" r:id="rId12"/>',
                     '<p:sldId id="270" r:id="rId13"/>']}

FIN_LECTURAS = {'primera_lectura':'''</a:t>
                                    </a:r>
                                </a:p>
                                <a:p>
                                    <a:pPr algn="just">
                                        <a:defRPr sz="2500">
                                            <a:latin typeface="+mj-lt"/>
                                            <a:ea typeface="+mj-ea"/>
                                            <a:cs typeface="+mj-cs"/>
                                            <a:sym typeface="Helvetica"/>
                                        </a:defRPr>
                                    </a:pPr>
                                    <a:r>
                                        <a:rPr dirty="0"/>
                                        <a:t>Palabra de Dios.                      </a:t>
                                    </a:r>
                                    <a:r>
                                        <a:rPr i="1" b="1" dirty="0"/>
                                        <a:t>R. Te alabamos Señor''',

                'segunda_lectura':'''</a:t>
                                    </a:r>
                                </a:p>
                                <a:p>
                                    <a:pPr algn="just">
                                        <a:defRPr sz="2500">
                                            <a:latin typeface="+mj-lt"/>
                                            <a:ea typeface="+mj-ea"/>
                                            <a:cs typeface="+mj-cs"/>
                                            <a:sym typeface="Helvetica"/>
                                        </a:defRPr>
                                    </a:pPr>
                                    <a:r>
                                        <a:rPr dirty="0"/>
                                        <a:t>Palabra de Dios.                      </a:t>
                                    </a:r>
                                    <a:r>
                                        <a:rPr i="1" b="1" dirty="0"/>
                                        <a:t>R. Te alabamos Señor''',

                'evangelio': '''</a:t>
                                </a:r>
                                </a:p>
                                <a:p>
                                    <a:pPr algn="just">
                                        <a:defRPr sz="2500">
                                            <a:latin typeface="+mj-lt"/>
                                            <a:ea typeface="+mj-ea"/>
                                            <a:cs typeface="+mj-cs"/>
                                            <a:sym typeface="Helvetica"/>
                                        </a:defRPr>
                                    </a:pPr>
                                    <a:r>
                                        <a:rPr dirty="0"/>
                                        <a:t>Palabra del Señor.                </a:t>
                                    </a:r>
                                    <a:r>
                                        <a:rPr b="1" dirty="0"/>
                                        <a:t>R. Gloria a ti Señor Jesús''',
                    'salmo' : ''}


if __name__ == '__main__':
    Hacedor(LECTURAS, PPT_BASE, PPT_FINAL, DIC, FIN_LECTURAS, SLIDE_SIZE, DIRS, FECHA, TITULO)
    subprocess.Popen("%s %s" % (office, PPT_FINAL))
   


    # if sys.platform.startswith('darwin'):
    #     subprocess.call(('open', PPT_FINAL))
    # elif os.name == 'nt':
    #     os.startfile(PPT_FINAL)
    # elif os.name == 'posix':
    #     subprocess.call(('xdg-open', PPT_FINAL))

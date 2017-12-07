# -*- coding: utf-8 -*-

from hacedor import *
import scrapper
# import subprocess, os
# import sys

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

#office = r"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"
#ENC = 'utf-8'
PPT_BASE = 'plantilla.xml'
PPT_FINAL = 'ppt_listo.xml'
SLIDE_SIZE = 740

DIRS = {}
LECTURAS = {}

TITULO = sys.argv[1]

# when extracts from web
if len(sys.argv) > 2:
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


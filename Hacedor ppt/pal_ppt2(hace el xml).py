primera_lectura = '''
 Si quieres, puedes
observar los mandamientos
y cumplir fielmente lo que
agrada al Señor. Él puso ante
ti el fuego y el agua: hacia
lo que quieras, extenderás tu mano. Ante
los hombres están la vida y la muerte:
a cada uno se le dará lo que prefiera.
Porque grande es la sabiduría del Señor,
él es fuerte y poderoso, y ve todas las
cosas. Sus ojos están fijos en aquellos que
lo temen y él conoce todas las obras del
hombre. A nadie le ordenó ser impío ni dio
a nadie autorización para pecar. 
'''

salmo = '''

R. Felices los que siguen la ley del Señor:
Felices los que van por un camino intachable,
los que siguen la ley del Señor.
Felices los que cumplen sus prescripciones
y lo buscan de todo corazón. R.
Tú promulgaste tus mandamientos para
que se cumplieran íntegramente. ¡Ojalá
yo me mantenga firme en la observancia
de tus preceptos! R.
Sé bueno con tu servidor, para que yo
viva y pueda cumplir tu palabra. Abre mis
ojos, para que contemple las maravillas
de tu ley. R.
Muéstrame, Señor, el camino de tus preceptos,
y yo los cumpliré a la perfección.
Instrúyeme, para que observe tu ley y la
cumpla de todo corazón. R.
'''

segunda_lectura = '''
Hermanos: Es verdad que
anunciamos una sabiduría
entre aquellos que son
personas espiritualmente maduras, pero
no la sabiduría de este mundo ni la que
ostentan los dominadores de este mundo,
condenados a la destrucción. Lo que
anunciamos es una sabiduría de Dios,
misteriosa y secreta, que él preparó para
nuestra gloria antes que existiera el mundo;
aquélla que ninguno de los dominadores de
este mundo alcanzó a conocer, porque si la
hubieran conocido no habrían crucificado al
Señor de la gloria. Nosotros anunciamos,
como dice la Escritura, “lo que nadie vio ni
oyó y ni siquiera pudo pensar, aquello que
Dios preparó para los que lo aman”. Dios
nos reveló todo esto por medio del Espíritu,
porque el Espíritu lo penetra todo, hasta lo
más íntimo de Dios. 
'''



evangelio = '''
Jesús dijo a sus discípulos:

No piensen que vine para abolir la Ley o los Profetas: Yo no he venido a abolir, sino a dar cumplimiento.

Les aseguro que no quedarán ni una i ni una coma de la Ley sin cumplirse, antes que desaparezcan el cielo y la tierra.

El que no cumpla el más pequeño de estos mandamientos, y enseñe a los otros a hacer lo mismo, será considerado el menor en el Reino de los Cielos. En cambio, el que los cumpla y enseñe, será considerado grande en el Reino de los Cielos.

Les aseguro que si la justicia de ustedes no es superior a la de los escribas y fariseos, no entrarán en el Reino de los Cielos.

Ustedes han oído que se dijo a los antepasados: “No matarás, y el que mata, debe ser llevado ante el tribunal”. Pero Yo les digo que todo aquél que se irrita contra su hermano, merece ser condenado por un tribunal. Y todo aquél que lo insulta, merece ser castigado por el Tribunal. Y el que lo maldice, merece el infierno.

Por lo tanto, si al presentar tu ofrenda en el altar, te acuerdas de que tu hermano tiene alguna queja contra ti, deja tu ofrenda ante el altar, ve a reconciliarte con tu hermano, y sólo entonces vuelve a presentar tu ofrenda.

Trata de llegar en seguida a un acuerdo con tu adversario, mientras vas caminando con él, no sea que el adversario te entregue al juez, y el juez al guardia, y te pongan preso. Te aseguro que no saldrás de allí hasta que hayas pagado el último centavo.

Ustedes han oído que se dijo: “No cometerán adulterio”. Pero Yo les digo: El que mira a una mujer deseándola, ya cometió adulterio con ella en su corazón.

Si tu ojo derecho es para ti una ocasión de pecado, arráncalo y arrójalo lejos de ti: es preferible que se pierda uno solo de tus miembros, y no que todo tu cuerpo sea arrojado al infierno. Y si tu mano derecha es para ti una ocasión de pecado, córtala y arrójala lejos de ti: es preferible que se pierda uno solo de tus miembros, y no que todo tu cuerpo sea arrojado al infierno.

También se dijo: “El que se divorcia de su mujer, debe darle una declaración de divorcio”. Pero Yo les digo: El que se divorcia de su mujer, excepto en caso de unión ilegal, la expone a cometer adulterio; y el que se casa con una mujer abandonada por su marido, comete adulterio.

Ustedes han oído también que se dijo a los antepasados: “No jurarás falsamente, y cumplirás los juramentos hechos al Señor”. Pero Yo les digo que no juren de ningún modo: ni por el cielo, porque es el trono de Dios; ni por la tierra, porque es el estrado de sus pies; ni por Jerusalén, porque es la Ciudad del gran Rey. No jures tampoco por tu cabeza, porque no puedes convertir en blanco o negro uno solo de tus cabellos.

Cuando ustedes digan “sí”, que sea sí, y cuando digan “no”, que sea no. Todo lo que se dice de más, viene del Maligno.
'''

def quitar_espacios(texto):
    texto = texto.replace('\n', ' ')
    texto = texto.replace('  ', ' ')
    texto = texto.replace('  ', ' ')
    return '    ' + texto.replace('  ', ' ') + '\n'


def separar_texto(texto):
    new_text = ''
    while len(texto) > 740:
        diap = texto[:740]
        i = len(diap) - diap[::-1].find('.')
        new_text +=  texto[:i] + '\n\n    '
        texto = texto[i:]
    return new_text + texto 

dic = { 'portada':['<p:sldId id="256" r:id="rId2"/>'], 
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

def escribidor(texto, lectura, xml, dic):
    texto = quitar_espacios(texto)
    texto = separar_texto(texto)
    l_lectura = texto.split('\n\n')
    if lectura == 'evangelio':
        l_lectura[-1] += '''</a:t>
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
                                        <a:t>R. Gloria a ti Señor Jesús'''
    elif lectura != 'salmo':
        l_lectura[-1] += '''</a:t>
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
                                        <a:t>R. Te alabamos Señor'''
    cant_diap = len(l_lectura)
    print(cant_diap, lectura)
    for i in range(cant_diap):
        reemplazar = lectura + str(i + 1)
        xml = xml.replace(reemplazar, l_lectura[i])
    cods = dic[lectura]
    for i in range(cant_diap, len(cods)):
        xml = xml.replace(cods[i], '')
    return xml
    


with open('probando ppt.xml', 'r', encoding='utf-8') as file3:
    xml = file3.read()
    xml = escribidor(primera_lectura, 'primera_lectura', xml, dic)
    xml = escribidor(salmo, 'salmo', xml, dic)
    xml = escribidor(segunda_lectura, 'segunda_lectura', xml, dic)
    xml = escribidor(evangelio, 'evangelio', xml, dic)
    with open('hola.xml', 'w', encoding='utf-8') as file2:
        file2.write(xml)


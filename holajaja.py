text = '''
La institución de la Pascua

1 Luego el Señor dijo a Moisés y a Aarón en la tierra de Egipto:

2 Este mes será para ustedes el mes inicial, el primero de los meses del año.

3 Digan a toda la comunidad de Israel: El diez de este mes, consíganse cada uno un animal del ganado menor, uno para cada familia.

4 Si la familia es demasiado reducida para consumir un animal entero, se unirá con la del vecino que viva más cerca de su casa. En la elección del animal tengan en cuenta, además del número de comensales, lo que cada uno come habitualmente.

5 Elijan un animal sin ningún defecto, macho y de un año; podrá ser cordero o cabrito.

6 Deberán guardarlo hasta el catorce de este mes, y a la hora del crepúsculo, lo inmolará toda la asamblea de la comunidad de Israel.

7 Después tomarán un poco de su sangre, y marcarán con ella los dos postes y el dintel de la puerta de las casas donde lo coman.

8 Y esa misma noche comerán la carne asada al fuego, con panes sin levadura y verduras amargas.

9 No la comerán cruda ni hervida, sino asada al fuego; comerán también la cabeza, las patas y las entrañas.

10 No dejarán nada para la mañana siguiente, y lo que sobre, lo quemarán al amanecer.

11 Deberán comerlo así: ceñidos con un cinturón, calzados con sandalias y con el bastón en la mano. Y lo comerán rápidamente: es la Pascua del Señor.

12 Esa noche yo pasaré por el país de Egipto para exterminar a todos sus primogénitos, tanto hombres como animales, y daré un justo escarmiento a los dioses de Egipto. Yo soy el Señor.

13 La sangre les servirá de señal para indicar las casas donde ustedes estén. Al verla, yo pasaré de largo, y así ustedes se libarán del golpe del Exterminador, cuando yo castigue al país de Egipto.

14 Este será para ustedes un día memorable y deberán solemnizarlo con una fiesta en honor del Señor. Lo celebrarán a lo largo de las generaciones como una institución perpetua.
'''
text2 = ''
for i in text:
    if not i.isdigit():
        text2 += i

print(text2)
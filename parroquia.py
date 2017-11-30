# -*- coding: utf-8-*-

a = 'Hermanos: Esta es la libertad que nos ha dado Cristo. Manténganse firmes para no caer de nuevo bajo el yugo de la esclavitud. Ustedes, hermanos, han sido llamados para vivir en libertad, pero procuren que esta libertad no sea un pretexto para satisfacer los deseos carnales: háganse más bien servidores los unos de los otros, por medio del amor. Porque toda la Ley está resumida plenamente en este precepto: Amarás a tu prójimo como a ti mismo. Pero si ustedes se están mordiendo y devorando mutuamente, tengan cuidado porque terminarán destruyéndose los unos a los otros. Yo los exhorto a que se dejen conducir por el Espíritu de Dios, y así no serán arrastrados por los deseos de la carne. Porque la carne desea contra el espíritu y el espíritu'
largo_max = 746

class Hojita:

    def __init__(self):
        with open('hojita.txt', 'r', encoding = 'utf-8') as file:
            self.text = file.read()

        self.largo_max = 745
        # limpiar
        self.text = self.text.replace('\n', ' ')
        self.text = self.text.replace('  ', ' ')

        self.primera_lectura = self.get_primera_lectura()
        self.salmo = self.get_salmo()
        self.segunda_lectura = self.get_segunda_lectura()
        print(self.segunda_lectura)
        self.evangelio = self.get_evangelio()
        self.escribir_todo()

    def escribir_todo(self):
        self.escribir(self.primera_lectura, 'Primera Lectura', 'w')
        self.escribir(self.salmo, 'Salmo', 'a')
        self.escribir(self.segunda_lectura, 'Segunda Lectura', 'a')
        self.escribir(self.evangelio, 'Evangelio', 'a')

    def escribir(self, text, titulo, metodo):
        with open('resultados.txt', metodo, encoding = 'utf-8') as file:
            file.write(titulo + '\n\n    ')
            while True:
                fin = text.find(' ', self.largo_max - 4)
                file.write(text[:fin] + '\n\n')
                text = text[fin:]
                print(len(text), 'y que pasa')
                if len(text) == 0 or len(text) == 1:
                    break

    def get_primera_lectura(self):
        return self.get('Lectura de', 'R. Te alabamos, Señor', 32, 23)

    def get_salmo(self):
        # se le agregan los enter despues de las r
        text = self.get('3. Salmo', '4. Segunda Lectura', 32, 3)
        text2 = text[:5]
        ultimo = '00'
        for i in text[5:]:
            text2 += i
            ultimo = ultimo[1:] + i
            if ultimo == 'R.':
                text2 += '\n   '
        return text2

    def get_segunda_lectura(self):
        return self.get('Lectura de la carta', 'R. Te alabamos, Señor', 50, 23)

    def get_evangelio(self):
        return self.get('Evangelio de nuestro ', 'Gloria a ti, Señor Jesús', 51, 24)

    def get(self, p_in, p_fin, parte_en = 0, termina_con = 0):
        inicio = self.text.find(p_in) + parte_en
        final = self.text.find(p_fin, inicio) + termina_con
        return self.text[inicio:final]

Hojita()

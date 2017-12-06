#from datos import *

def remove_spaces(text):
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    text = text.replace('  ', ' ')
    return text.rstrip()


class Hacedor:
    def __init__(self, lecturas, raw_ppt, modified_ppt, slides_codes, ends, slide_size, dirs, date, title):
        enc = 'utf-8'
        self.lecturas = lecturas
        self.slides_codes = slides_codes
        self.ends = ends
        self.slide_size = slide_size
        self.dirs = dirs
        self.date = date
        self.title = title

        with open(raw_ppt, encoding=enc) as raw:
            self.xml = raw.read()
            self.modify_file()
        with open(modified_ppt, 'w', encoding=enc) as final:
            self.write_file(final)

    def modify_file(self):
        self.names = ['primera_lectura', 'salmo', 
                'segunda_lectura', 'evangelio']
        for name in self.names:
            text = self.lecturas[name]
            self.name = name
            self.text = text
            self.modifier()
            self.replace_dirs()
            self.title_date()

    def title_date(self):
        self.xml = self.xml.replace('titulo_ppt', self.title)
        self.xml = self.xml.replace('fecha_ppt', self.date)

    def write_file(self, file):
        file.write(self.xml)

    def modifier(self):
        self.remove_spaces()
        self.add_details()
        # the begginning of the editino of the salmo
        if self.name == 'salmo':
            self.text = self.text.replace('. R. ', '. R.')
            self.text = self.text.replace('! R. ', '! R.')
            a = '</a:t></a:r><a:r><a:rPr lang="es-CL" b="1" dirty="0"/><a:t>'
            z = '</a:t></a:r><a:r><a:rPr lang="es-CL" dirty="0"/><a:t> </a:t></a:r></a:p><a:p><a:pPr algn="just"><a:spcBef><a:spcPts val="600"/></a:spcBef><a:spcAft><a:spcPts val="600"/></a:spcAft><a:defRPr sz="2500"><a:latin typeface="+mj-lt"/><a:ea typeface="+mj-ea"/><a:cs typeface="+mj-cs"/><a:sym typeface="Helvetica"/></a:defRPr></a:pPr><a:r><a:rPr lang="es-CL" dirty="0"/><a:t>'
            self.text = self.text.replace('R.', a + 'R.' + z)
            a2 = '<a:p><a:pPr algn="just"><a:spcBef><a:spcPts val="600"/></a:spcBef><a:spcAft><a:spcPts val="600"/></a:spcAft><a:defRPr sz="2500"><a:latin typeface="+mj-lt"/><a:ea typeface="+mj-ea"/><a:cs typeface="+mj-cs"/><a:sym typeface="Helvetica"/></a:defRPr></a:pPr><a:r><a:rPr lang="es-CL" b="1" dirty="0"/><a:t>'
            z2 = '</a:t></a:r></a:p><a:p><a:pPr algn="just"><a:spcBef><a:spcPts val="600"/></a:spcBef><a:spcAft><a:spcPts val="600"/></a:spcAft><a:defRPr sz="2500"><a:latin typeface="+mj-lt"/><a:ea typeface="+mj-ea"/><a:cs typeface="+mj-cs"/><a:sym typeface="Helvetica"/></a:defRPr></a:pPr><a:r><a:rPr lang="es-CL" dirty="0"/><a:t>'
            self.text = self.text.replace('R/.', a2 + 'R.')
            self.text = self.text.replace('santiago hizo esto ', z2)
            self.text += '</a:t></a:r>'
            self.diaps_l = [self.text]
            print('wassaaa')
        else:
            self.separate_text()

        self.cant_diap = len(self.diaps_l)
        self.add_end()
        
        self.replacing()
        # self.replace_dirs()
        self.del_diaps()

    def remove_spaces(self):
        self.text = remove_spaces(self.text)

    def add_details(self):
        self.text = '   '+ self.text +'\n'

    def replace_dirs(self):
        der = self.name + '_dir'
        reemp = self.dirs[self.name]
        reemp = remove_spaces(reemp)
        self.xml = self.xml.replace(der, reemp)

    def separate_text(self):
        t = self.text
        ss = self.slide_size
        new_text = ''
        while len(t) > ss:
            diap = t[:ss]
            i = len(diap) - diap[::-1].find('.')
            new_text +=  t[:i] + '\n\n    '
            t = t[i:]
        separated_text = new_text + t
        self.diaps_l = separated_text.split('\n\n')   

    def add_end(self):
        self.diaps_l[-1] += self.ends[self.name]

    def replacing(self): 
        d = self.diaps_l
        for i in range(self.cant_diap):
            # la cagada por culpa del salmo
            if self.name == 'salmo':
                a = '<a:p><a:pPr algn="just"><a:spcBef><a:spcPts val="600"/></a:spcBef><a:spcAft><a:spcPts val="600"/></a:spcAft><a:defRPr sz="2500"><a:latin typeface="+mj-lt"/><a:ea typeface="+mj-ea"/><a:cs typeface="+mj-cs"/><a:sym typeface="Helvetica"/></a:defRPr></a:pPr><a:r><a:rPr lang="es-CL" dirty="0"/><a:t>'
                z = '</a:t></a:r>'
                reemp = a + 'salmo1' + z
            else:
                reemp = self.name + str(i + 1)
            self.xml = self.xml.replace(reemp, d[i])

    def del_diaps(self):
        cods = self.slides_codes[self.name]
        for i in range(self.cant_diap, len(cods)):
            self.xml = self.xml.replace(cods[i], '')


#self, lecturas, raw_ppt, modified_ppt, self.slides_codes, self.ends, slide_size
if __name__ == '__main__':
    Hacedor(LECTURAS, PPT_BASE, PPT_FINAL, DIC, FIN_LECTURAS, SLIDE_SIZE, DIRS)
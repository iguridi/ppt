import ppt


def format_addr(addr):
    addr = addr.strip()
    addr = '(' + addr + ')'
    return addr


def remove_spaces(text):
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('  ', ' ')
    return text.rstrip()


class Reading:
    # in charge of all text-related things.
    def __init__(self, title, addrs, body):
        self.title = title
        self.addrs = format_addr(addrs)
        self.body = body
        # list of the text splited into chunks of a predifined max chars
        self.slides = []
        self.make_pretty()

    def make_pretty(self):
        self.body = remove_spaces(self.body)
        self.body = '	' + self.body + '\n'

    def __repr__(self):
        return (self.title, self.addrs, self.body)


class Psalm(Reading):
    '''
	Is harder to format the psalm text so it has its own class and functions
	Arguments:
		* Same as his parent: Reading()
	'''
    def __init__(self, title, addrs, body):
        super().__init__(title, addrs, body)
        self.response = ''
        self.paragraphs = []
        self.make_pretty()
        self.split_paragraphs()

    def make_pretty(self):
        self.body = remove_spaces(self.body)
        self.body = self.body.replace('R/. ', 'R. ')
        self.body = self.body.replace('. R. ', '. R.')
        self.body = self.body.replace('! R. ', '! R.')

    def split_paragraphs(self):
        '''
		Spliting the psalm`s paragraphs is needed for adding the "R." at the end of each.
		'''
        self.response = self.body[:self.body.find('***')]
        pars_pos = self.body.find('***') + 3
        self.body = self.body[pars_pos:]
        self.paragraphs = self.body.split(' R.')
        del self.paragraphs[-1]
        for n, _ in enumerate(self.paragraphs):
            self.paragraphs[n] = '	' + self.paragraphs[n]


class Maker:
    '''
	In charge of making and formating the slides.
	Arguments:
		* base_ppt (string): name of the ppt with the layouts
		* output_ppt (string): name of the  ppt to modify
		* slide_size (int): ideal maximum of characters in a slide
		* addrs (list(string)): readings bible addresses
		* readings (list(string)): lectures themselves
		* ppt_title (string): title of the presentation based on the celebration on that *date
		* date (string): Date of the mass
	'''
    def __init__(
        self,
        base_ppt,
        output_ppt,
        slide_size,
        addrs,
        readings,
        ppt_title=None,
        date=None,
    ):
        self.readings = readings
        self.slide_size = slide_size
        self.addrs = addrs
        self.date = date
        self.ppt_title = ppt_title
        # create ppt and save
        self.ppt = ppt.Ppt(base_ppt)
        self.process()
        self.ppt.save(output_ppt)

    def process(self):
        '''
		The process of making and formating the ppt.
		'''
        names = ['primera_lectura', 'salmo', 'segunda_lectura', 'evangelio']
        self.ppt.make_cover(self.ppt_title, self.date)
        for name in names:
            if name != 'salmo':
                if name == 'segunda_lectura':
                    try:
                        self.readings[name]
                    except KeyError:
                        continue
                reading = Reading(name, self.addrs[name],
                                       self.readings[name])
            else:
                reading = Psalm(name, self.addrs[name],
                                     self.readings[name])
            self.separate_text(reading)
            self.make_readings_slides(reading)
        self.add_extra_slides()

    def separate_text(self, reading):
        '''
		Split the text into various slides depending of the text length
		'''
        t = reading.body
        new_text = ''
        while len(t) > self.slide_size:
            diap = t[:self.slide_size]
            i = len(diap) - diap[::-1].find('.')
            new_text += t[:i] + '\n\n    '
            t = t[i:]
        separated_text = new_text + t
        reading.slides = separated_text.split('\n\n')

    def make_readings_slides(self, reading):
        '''
		Add the actual slides and its text and address and ending
		'''
        if reading.title == ppt.PSALM:
            self.ppt.add_psalm(reading)
        else:
            self.ppt.add_reading(reading)

    def add_extra_slides(self):
        self.ppt.add_slide(ppt.PICTURE)
        self.ppt.add_slide(ppt.ANNOUNCEMENTS)
        self.ppt.add_slide(ppt.PICTURE)

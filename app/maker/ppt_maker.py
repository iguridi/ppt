import ppt

SLIDE_SIZE = 730


def format_addr(addr):
    addr = addr.strip()
    addr = '(' + addr + ')'
    return addr


def remove_spaces(text):
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    text = text.replace('  ', ' ')
    return text.rstrip()

class MassPart:
    def add_itself_to_ppt(self, ppt):
        raise Exception('method add_itself_to_ppt not implemented')

class Reading(MassPart):
    def __init__(self, title, addrs, body):
        self.title = title
        self.addrs = format_addr(addrs)
        self.body = body
        # list of the text splited into chunks of a predifined max chars
        self.make_pretty()
        self.slides = self.separate_text()

    def make_pretty(self):
        self.body = remove_spaces(self.body)
        self.body = '	' + self.body + '\n'

    def add_itself_to_ppt(self, ppt):
        for i, slide_text in enumerate(self.slides):
            slide = ppt.add_slide(self.title)
            address = slide.placeholders[12]  # placeholder idx of the address
            body = slide.placeholders[10]  # placeholder idx of the body text
            # the address is the same for all
            address.text = self.addrs

            body.text = slide_text
            if i == len(self.slides) - 1: # the last slide of this part
                ppt.add_readings_ends(slide, self)

    def separate_text(self):
        '''
		Split the text into various slides depending of the text length
		'''
        t = self.body
        new_text = ''
        while len(t) > SLIDE_SIZE:
            diap = t[:SLIDE_SIZE]
            i = len(diap) - diap[::-1].find('.')
            new_text += t[:i] + '\n\n    '
            t = t[i:]
        separated_text = new_text + t
        return separated_text.split('\n\n')

    def __repr__(self):
        return (self.title, self.addrs, self.body)


class Cover(MassPart):
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def add_itself_to_ppt(self, presentation):
        cover = presentation.add_slide(ppt.COVER)
        title_placeholder = cover.shapes.title  # placeholder idx of the address
        date_placeholder = cover.placeholders[
            10]  # placeholder idx of the body
        title_placeholder.text = self.title
        date_placeholder.text = self.date


class Picture(MassPart):
    def add_itself_to_ppt(self, presentation):
        presentation.add_slide(ppt.PICTURE)


class Announcements(MassPart):
    def add_itself_to_ppt(self, presentation):
        presentation.add_slide(ppt.ANNOUNCEMENTS)


class Psalm(Reading):
    def __init__(self, title, addrs, body):
        super().__init__(title, addrs, body)
        self.response = ''
        self.paragraphs = []
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

    def add_itself_to_ppt(self, ppt):
        slide = ppt.add_slide(self.title)
        address = slide.placeholders[12]  # placeholder idx of the address
        body = slide.placeholders[10]  # placeholder idx of the body text
        # the address is the same for all
        address.text = self.addrs
        txt_fm = body.text_frame
        # add the response bold text at the beggining
        resp = txt_fm.paragraphs[0]
        resp.text = self.response
        font = resp.font
        font.bold = True
        for paragraph in self.paragraphs:
            # add each paragraph of the psalm
            par = txt_fm.add_paragraph()
            par.text = paragraph
            run = par.add_run()
            run.text = ' R.'
            font = run.font
            font.bold = True


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
        addrs,
        readings,
        ppt_title=None,
        date=None,
    ):
        self.readings = readings
        self.addrs = addrs
        self.date = date
        self.ppt_title = ppt_title
        # create ppt and save in new file
        self.ppt = ppt.Ppt(base_ppt)
        self.build_ppt()
        self.ppt.save(output_ppt)

    def build_ppt(self):
        mass_parts = []
        mass_parts.append(Cover(self.ppt_title, self.date))
        for name in self.readings.keys():
            if name == 'salmo':
                reading = Psalm(name, self.addrs[name], self.readings[name])
            else:
                reading = Reading(name, self.addrs[name], self.readings[name])
            mass_parts.append(reading)
        mass_parts.append(Picture())
        mass_parts.append(Announcements())
        mass_parts.append(Picture())
        for part in mass_parts:
            part.add_itself_to_ppt(self.ppt)

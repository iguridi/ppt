from pptx import Presentation

COVER = 'portada'
FIRST_LECTURE = 'primera_lectura'
PSALM = 'salmo'
SECOND_LECTURE = 'segunda_lectura'
GOSPEL = 'evangelio'
ANNOUNCEMENTS = 'anuncios'
PICTURE = 'imagen'

LAYOUTS_INDEX = {
    COVER: 0,
    FIRST_LECTURE: 1,
    PSALM: 2,
    SECOND_LECTURE: 3,
    GOSPEL: 4,
    ANNOUNCEMENTS: 5,
    PICTURE: 6,
}

ENDINGS = {
    FIRST_LECTURE: ('Palabra de Dios', 'Te alabamos Señor'),
    SECOND_LECTURE: ('Palabra de Dios', 'Te alabamos Señor'),
    GOSPEL: ('Palabra del Señor', 'Gloria a ti, Señor Jesús')
}


class Ppt:
    def __init__(self, base_ppt):
        self.prs = Presentation(base_ppt)

    def get_slide_layout(self, name):
        return self.prs.slide_layouts[LAYOUTS_INDEX[name]]

    def add_slide(self, name):
        return self.prs.slides.add_slide(self.get_slide_layout(name))

    def save(self, output_ppt):
        self.prs.save(output_ppt)

    def add_psalm(self, psalm):
        slide = self.add_slide(psalm.title)
        address = slide.placeholders[12]  # placeholder idx of the address
        body = slide.placeholders[10]  # placeholder idx of the body text
        # the address is the same for all
        address.text = psalm.addrs
        # setting up the text of the body of the psalm is different beacause its formatting
        # if self.reading.title == 'salmo':
        txt_fm = body.text_frame
        # add the response bold text at the beggining
        # the default paragraph has white space. Dont have to add a new one, you have to use it
        resp = txt_fm.paragraphs[0]
        resp.text = psalm.response
        font = resp.font
        font.bold = True
        for paragraph in psalm.paragraphs:
            # add each paragraph of the psalm
            par = txt_fm.add_paragraph()
            par.text = paragraph
            run = par.add_run()
            run.text = ' R.'
            font = run.font
            font.bold = True

    def add_readings_ends(self, slide, reading):
        dialog_father = slide.placeholders[13]
        character = slide.placeholders[17]
        dialog_people = slide.placeholders[16]

        dialog_father.text = ENDINGS[reading.title][0]
        character.text = 'R.'
        dialog_people.text = ENDINGS[reading.title][1]

    def make_cover(self, title, date):
        cover = self.add_slide(COVER)
        title_placeholder = cover.shapes.title  # placeholder idx of the address
        date_placeholder = cover.placeholders[
            10]  # placeholder idx of the body
        title_placeholder.text = title
        date_placeholder.text = date

    def add_reading(self, reading):
        for i, slide_text in enumerate(reading.slides):
            slide = self.add_slide(reading.title)
            address = slide.placeholders[12]  # placeholder idx of the address
            body = slide.placeholders[10]  # placeholder idx of the body text
            # the address is the same for all
            address.text = reading.addrs

            body.text = slide_text
            if i == len(reading.slides) - 1:
                self.add_readings_ends(slide, reading)
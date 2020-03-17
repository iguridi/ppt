from pptx import Presentation

COVER = 'portada'
FIRST_LECTURE = 'primera_lectura'
PSALM = 'salmo'
SECOND_LECTURE = 'segunda_lectura'
GOSPEL = 'evangelio'
ANNOUNCEMENTS = 'anuncios'
PICTURE = 'imagen'

ADDRES_PH_INDEX = 12
BODY_PH_INDEX = 10

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

    def add_readings_ends(self, slide, reading):
        dialog_father = slide.placeholders[13]
        character = slide.placeholders[17]
        dialog_people = slide.placeholders[16]

        dialog_father.text = ENDINGS[reading.title][0]
        character.text = 'R.'
        dialog_people.text = ENDINGS[reading.title][1]

from typing import List, Dict

from app import ppt

SLIDE_SIZE = 690

ENDINGS = {
    ppt.FIRST_LECTURE: ("Palabra de Dios", "Te alabamos Señor"),
    ppt.SECOND_LECTURE: ("Palabra de Dios", "Te alabamos Señor"),
    ppt.GOSPEL: ("Palabra del Señor", "Gloria a ti, Señor Jesús"),
}


def format_addr(addr: str) -> str:
    addr = addr.strip()
    addr = "(" + addr + ")"
    return addr


class MassPart:
    def add_itself_to_ppt(self, ppt: ppt.Ppt):
        raise Exception("method add_itself_to_ppt not implemented")


class Reading(MassPart):
    def __init__(self, title: str, addrs: str, body: str):
        self.title = title
        self.addrs = format_addr(addrs)
        self.body = "	" + body
        # list of the text splited into chunks of a predifined max chars
        self.slides = self.separate_text()

    def add_itself_to_ppt(self, ppt: ppt.Ppt):
        for i, slide_text in enumerate(self.slides):
            slide = ppt.add_slide(self.title)
            address = slide.placeholders[12]  # placeholder idx of the address
            body = slide.placeholders[10]  # placeholder idx of the body text
            # the address is the same for all
            address.text = self.addrs

            body.text = slide_text
            if i == len(self.slides) - 1:  # the last slide of this part
                dialog_father = slide.placeholders[13]
                character = slide.placeholders[17]
                dialog_people = slide.placeholders[16]

                dialog_father.text = ENDINGS[self.title][0]
                character.text = "R."
                dialog_people.text = ENDINGS[self.title][1]

    def separate_text(self) -> List[str]:
        """
		Split the text into various slides depending of the text length
		"""
        t = self.body
        new_text = ""
        while len(t) > SLIDE_SIZE:
            diap = t[:SLIDE_SIZE]
            i = len(diap) - diap[::-1].find(".")
            new_text += t[:i] + "\n\n    "
            t = t[i:]
        separated_text = new_text + t
        return separated_text.split("\n\n")

    def __repr__(self):
        return (self.title, self.addrs, self.body)


class Cover(MassPart):
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def add_itself_to_ppt(self, presentation):
        cover = presentation.add_slide(ppt.COVER)
        title_placeholder = cover.shapes.title  # placeholder idx of the address
        date_placeholder = cover.placeholders[10]  # placeholder idx of the body
        title_placeholder.text = self.title
        date_placeholder.text = self.date


class Picture(MassPart):
    def add_itself_to_ppt(self, presentation: ppt.Ppt):
        presentation.add_slide(ppt.PICTURE)


class Announcements(MassPart):
    def add_itself_to_ppt(self, presentation: ppt.Ppt):
        presentation.add_slide(ppt.ANNOUNCEMENTS)


class Psalm(Reading):
    def __init__(self, title: str, addrs: str, body: str):
        super().__init__(title, addrs, body)
        self.make_pretty()
        self.response = ""
        self.paragraphs = []
        self.split_paragraphs()

    def make_pretty(self):
        self.body = self.body.replace("R/. ", "")
        self.body = self.body.replace(". R. ", ". R.")
        self.body = self.body.replace("! R. ", "! R.")

    def split_paragraphs(self):
        """
		Spliting the psalm`s paragraphs is needed for adding the "R." at the end of each.
		"""
        end_response = self.body.find(" R.")
        self.response = self.body[:end_response]
        body = self.body[end_response + 3 :]
        self.paragraphs = body.split(" R.")
        del self.paragraphs[-1]
        for n, _ in enumerate(self.paragraphs):
            self.paragraphs[n] = "	" + self.paragraphs[n]

    def add_itself_to_ppt(self, ppt: ppt.Ppt):
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
            run.text = " R."
            font = run.font
            font.bold = True


class Maker:
    """
	In charge of making and formating the slides.
	Arguments:
		* base_ppt (string): name of the ppt with the layouts
		* output_ppt (string): name of the  ppt to modify
		* slide_size (int): ideal maximum of characters in a slide
		* addrs (list(string)): readings bible addresses
		* readings (list(string)): lectures themselves
		* ppt_title (string): title of the presentation based on the celebration on that *date
		* date (string): Date of the mass
	"""

    def __init__(
        self,
        base_ppt: str,
        output_ppt: str,
        addrs: Dict[str, str],
        readings: Dict[str, str],
        ppt_title: str = None,
        date: str = None,
    ):
        self.readings = readings
        self.addrs = addrs
        self.date = date
        self.ppt_title = ppt_title
        # create ppt and save in new file
        self.ppt = ppt.Ppt(base_ppt)
        self.build_ppt()
        self.ppt.save(output_ppt)

    def is_sunday(self):
        return ppt.SECOND_LECTURE in self.readings

    def build_ppt(self):
        mass_parts = []
        mass_parts.append(Cover(self.ppt_title, self.date))

        mass_part_names = [ppt.FIRST_LECTURE, ppt.PSALM, ppt.GOSPEL]
        if self.is_sunday():
            mass_part_names = [
                ppt.FIRST_LECTURE,
                ppt.PSALM,
                ppt.SECOND_LECTURE,
                ppt.GOSPEL,
            ]
        for name in mass_part_names:
            if name == ppt.PSALM:
                reading = Psalm(name, self.addrs[name], self.readings[name])
            else:
                reading = Reading(name, self.addrs[name], self.readings[name])
            mass_parts.append(reading)

        mass_parts.append(Picture())
        mass_parts.append(Announcements())
        mass_parts.append(Picture())
        for part in mass_parts:
            part.add_itself_to_ppt(self.ppt)

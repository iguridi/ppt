from pptx import Presentation

def remove_spaces(text):
	text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    text = text.replace('  ', ' ')
    return text.rstrip()

class Maker:
	ENCODING = 'utf-8'	
	def __init__(self, lectures, base_ppt, output_ppt, slide_size, addrs, date, ppt_title):
		self.lectures = lectures
		self.slide_size = slide_size
		self.addrs = addrs
		self.date = date
		self.ppt_title = ppt_title

		self.prs = Presentation(base_ppt)
		self.modify_file()
		self.prs.save(output_ppt)

	def modify_process(self):
		names = ['primera_lectura',
				 'salmo',
				 'segunda_lectura',
				 'evangelio'
				 ]
		for name in names:
			self.name = name
			self.text = self.lecturas[name]
			self.prettier()
			

	def prettier(self):
		self.text = remove_spaces(self.text)
		self.text = '	' +  self.text + '\n'

	def separate_text(self):
		t = self.text
        new_text = ''
        while len(t) > self.slide_size:
            diap = t[:self.slide_size]
            i = len(diap) - diap[::-1].find('.')
            new_text +=  t[:i] + '\n\n    '
            t = t[i:]
        separated_text = new_text + t
        self.diaps_l = separated_text.split('\n\n')




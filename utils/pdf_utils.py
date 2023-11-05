from fpdf import FPDF
import math
from models.empresa import Empresa
#from PIL import Image
import os

class PDF(FPDF):
    def __init__(self, orientation = 'P', unit = 'mm', pdf_format='A4', filename = 'report.pdf'):
        super().__init__(orientation, unit, pdf_format)
        self.filename = filename
        self.empresa = Empresa().getEmpresa()
        self.logo = os.path.join(self.empresa.getLogo())
        self.title = ''
        print('Creando PDF...')

    def set_pdf_title(self, title):
        self.title = title
    
    def set_filename(self, filename):
        self.filename = filename

    def get_filename(self):
        return self.filename

    def header(self):
        logo_width = 64
        logo_height = 24
        linea = 20
        height = 4
        self.rect(20, 20, 180, logo_height)
        # Logo
        #print(type(self.logo))
        #logo = Image.open(self.logo)
        #width, height = logo.size
        #logo_width = int((logo_height / float(height)) * width)
        self.image(self.logo, 20, 20, logo_width, logo_height)
        self.rect(20, 20, logo_width, logo_height)
        #Datos de la empresa
        nombre_empresa = str(self.empresa.getName())
        direccion1 = str(self.empresa.getDireccion1())
        direccion2 = str(self.empresa.getDireccion2())
        ciudad = str(self.empresa.getCiudad())
        estado = str(self.empresa.getEstado())
        RIF = str(self.empresa.getRIF())
        self.set_font('Arial', '', 9)
        self.set_xy(25 + logo_width, linea)
        self.cell(200 - logo_width, 10, nombre_empresa, 0, 0, 'L')
        linea+=height
        self.set_font('Arial', '', 8)
        self.set_xy(25 + logo_width, linea)
        self.cell(200 - logo_width, 10, direccion1, 0, 0, 'L')
        linea+=height
        self.set_xy(25 + logo_width, linea)
        self.cell(200 - logo_width, 10, direccion2, 0, 0, 'L')
        linea+=height
        self.set_xy(25 + logo_width, linea)
        self.cell(200 - logo_width, 10, ciudad + " - " + estado, 0, 0, 'L')
        linea+=height
        self.set_xy(25 + logo_width, linea)
        self.cell(200 - logo_width, 10, RIF, 0, 0, 'L')
        linea+=height

        # Line breaks
        self.ln(25)

    def set_logo(self, logo_path):
        self.logo = logo_path

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
    
    def open_PDF(self):
        print('Opening')
        os.startfile(self.filename)

    def estimate_lines_needed(self, col_width: float, iter) -> int:
        """_summary_

        Args:
            iter (iterable): a row in your table
            col_width (float): cell width

        Returns:
            _type_: _description_
        """
        font_width_in_mm = (
            self.font_size_pt * 0.35 * 0.6
        )  # assumption: a letter is half his height in width, the 0.5 is the value you want to play with
        max_cell_text_len_header = max([len(str(col)) for col in iter])  # how long is the longest string?
        return math.ceil(max_cell_text_len_header * font_width_in_mm / col_width)

    def nb_lines(self, width, text):
        # one pt is ~0.35mm
        # font size is in pt
        lines = 0
        text_width = len(str(text))
        if (text_width < width):
            lines = 1
        else:
            i = 0
            for char in enumerate(text):
                i += 1
                if i > text_width:
                    lines+=1
                    i=0
        return lines

from utils.database import DB
from utils.pdf_utils import PDF

def exportar_pdf_productos():
    db = DB()
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_title('Lista de Productos')

    data = db.select('tbl_subproductos')
    height = 4.5

    pdf.header()

    posY = 50

    # Arial bold 14
    pdf.set_font('Arial', 'B', 14)
    pdf.set_xy(20, posY)
    pdf.cell(170, 10, 'Lista de Productos', 0, 0, 'C')
    posY += 10
    pdf.set_font('Arial', 'B', 9)
    pdf.set_xy(20, posY)
    pdf.cell(10, height, 'ID', 1, 1, 'C')
    pdf.set_xy(30,posY)  
    pdf.cell(65, height, 'Nombre', 1, 1, 'L')
    pdf.set_xy(95,posY)
    pdf.cell(20, height, 'Cantidad', 1, 1, 'C')
    pdf.set_xy(115,posY)
    pdf.cell(25, height, 'Costo Unitario', 1, 1, 'C')
    pdf.set_xy(140,posY)
    pdf.cell(20, height, 'Costo Total', 1, 1, 'C')
    pdf.set_xy(160,posY)
    pdf.cell(40, height, 'Fecha Ingreso', 1, 1, 'C')

    posY = posY + height

    for index, row in enumerate(data):      
        if row[5] != None:
            costo_unitario = str(round(float(row.get('costo_unitario')))) 
        else:
            costo_unitario = str(0.00)

        if row[6] != None:
            costo_total = str(round(float(row[6]))) 
        else:
            costo_total = str(0.00)

        
        lines = pdf.estimate_lines_needed(65, str(row[2]))
        print(lines)

        pdf.set_font('Arial', '', 9)
        pdf.set_xy(20, posY)
        pdf.cell(10, height, str(index + 1), 1, 1, 'C')
        pdf.set_xy(30,posY)  
        pdf.set_font('Arial', '', 8)
        lineheight = pdf.font_size * 2.5
        print(lineheight)
        if lines > 1:
            height = lines * lineheight
        print(height)
        pdf.multi_cell(65, height, str(row[2]), 1, 'L', 0)
        pdf.set_font('Arial', '', 9)
        pdf.set_xy(95,posY)
        pdf.cell(20, height, str(row[4]), 1, 1, 'C')
        pdf.set_xy(115,posY)
        pdf.cell(25, height, costo_unitario, 1, 1, 'R')
        pdf.set_xy(140,posY)
        pdf.cell(20, height, costo_total, 1, 1, 'R')
        pdf.set_xy(160,posY)
        pdf.cell(40, height, str(row[11]), 1, 1, 'C')

        posY = posY + height
    
    print('Datos pintados')
    pdf.footer()

    filename = 'Productos.pdf'

    pdf.output(filename, 'F')
    pdf.set_filename(filename)
    pdf.open_PDF()

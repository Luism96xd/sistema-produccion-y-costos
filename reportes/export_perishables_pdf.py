from utils.database import DB
from utils.pdf_utils import PDF
from models.categoria import Categoria
from datetime import datetime


def exportar_pdf_perecederos():
    db = DB()
    pdf = PDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.alias_nb_pages()
    pdf.set_title('Lista de Productos Perecederos')

    data = db.select('tbl_subproductos')
    data.sort(key=lambda x: x.get('fecha_ingreso'))

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
    pdf.cell(15, height, 'Código', 1, 1, 'C')
    pdf.set_xy(35,posY)  
    pdf.cell(25, height, 'Categoría', 1, 1, 'C')
    pdf.set_xy(60,posY)
    pdf.cell(40, height, 'Nombre', 1, 1, 'L')
    pdf.set_xy(100,posY)
    pdf.cell(20, height, 'Cantidad', 1, 1, 'C')
    pdf.set_xy(120,posY)
    pdf.cell(25, height, 'Fecha Ingreso', 1, 1, 'C')
    pdf.set_xy(145,posY)
    pdf.cell(25, height, 'Vida Útil', 1, 1, 'C')
    pdf.set_xy(170,posY)
    pdf.cell(30, height, 'Estatus', 1, 1, 'C')

    posY = posY + height

    for index, row in enumerate(data):      
        codigo = row.get('codigo_producto')
        id_categoria = row.get('id_categoria')
        nombre = row.get('nombre_producto')
        cantidad = row.get('cantidad')
        fecha_ingreso = row.get('fecha_ingreso').strftime('%Y-%m-%d')
        vida_util = row.get('vida_util')
        id_categoria = row.get('id_categoria')
        categoria = Categoria.get_name_by_id(id_categoria)
        status_item = ""
            
        days_diff = abs((datetime.today() - row.get('fecha_ingreso')).days)


        pdf.set_font('Arial', '', 9)

        pdf.set_xy(20, posY)
        pdf.cell(15, height, codigo, 1, 1, 'C')
        pdf.set_xy(35,posY)  
        pdf.cell(25, height, categoria, 1, 1, 'C')
        pdf.set_xy(60,posY)
        pdf.cell(40, height, nombre, 1, 1, 'L')
        pdf.set_xy(100,posY)
        pdf.cell(20, height, str(cantidad), 1, 1, 'C')
        pdf.set_xy(120,posY)
        pdf.cell(25, height, fecha_ingreso, 1, 1, 'C')
        pdf.set_xy(145,posY)
        pdf.cell(25, height, str(vida_util), 1, 1, 'C')

        if days_diff >= vida_util:
            pdf.set_fill_color(255, 0, 0)
            status_item = 'Expired'
        elif days_diff >= (vida_util / 2) and days_diff < vida_util:
            pdf.set_fill_color(255, 255, 0)
            status_item = 'Near'
        else:
            pdf.set_fill_color(255, 255, 255)
            status_item = 'OK'

        pdf.set_xy(170,posY)
        pdf.cell(30, height, status_item, 1, 1, 'C', fill=True)


        posY = posY + height
    
    print('Datos pintados')
    pdf.footer()

    filename = 'Productos.pdf'

    pdf.output(filename, 'F')
    pdf.set_filename(filename)
    pdf.open_PDF()

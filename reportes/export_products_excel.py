from utils.excel_utils import Spreadsheet
from utils.database import DB
from openpyxl.utils import get_column_letter

def exportar_excel_productos():
    db = DB()
    spreadsheet = Spreadsheet()
    sheet = spreadsheet.get_active_sheet()

    data = db.select_all('tbl_subproductos')

    row_count = len(data)

    sheet['A1'] = 'PRODUCTO ID'
    sheet['B1'] = 'NOMBRE'
    sheet['C1'] = 'DESCRIPCION'
    sheet['D1'] = 'CANTIDAD'
    sheet['E1'] = 'COSTO UNITARIO'
    sheet['F1'] = 'COSTO TOTAL'
    sheet['G1'] = 'CÓDIGO'
    sheet['H1'] = 'MARCA'
    sheet['I1'] = 'MODELO'
    sheet['J1'] = 'FECHA CREACIÓN'

    for index, row in enumerate(data):
        sheet[f'A{2 + index}'] = row[0]
        sheet[f'B{2 + index}'] = row[2]
        sheet[f'C{2 + index}'] = row[3]
        sheet[f'D{2 + index}'] = row[4]
        sheet[f'E{2 + index}'] = row[5]
        sheet[f'F{2 + index}'] = row[6]
        sheet[f'G{2 + index}'] = row[7]
        sheet[f'h{2 + index}'] = row[8]
        sheet[f'I{2 + index}'] = row[9]
        sheet[f'J{2 + index}'] = row[11]
    

    for i, value in enumerate(spreadsheet.get_active_sheet().columns):  # ,1 to start at 1
        if type(value) == str:
            column_width = len(value)
        else:
            column_width = 20
        spreadsheet.get_active_sheet().column_dimensions[get_column_letter(1 + i)].width = column_width

    spreadsheet.set_borders(row_count = row_count)
    spreadsheet.set_alignment(row_count = row_count)

    spreadsheet.set_title('Productos')
    spreadsheet.set_filename('productos.xlsx')

    spreadsheet.save()
    spreadsheet.open_spreadsheet()

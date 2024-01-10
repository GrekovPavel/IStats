from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from app.Grid import Grid
from app.Command import Command
import sys

class Pdf:
    def create_pdf(self):
        grid = Grid()
        print(grid.headers)
        sys.exit()

        grid.set_headers()
        print(grid.get_headers())
        pdfmetrics.registerFont(TTFont('DejaVuSans', 'fonts/DejaVuSans.ttf'))

        pdf = SimpleDocTemplate("result.pdf", pagesize=letter)

        table_data = [grid.get_headers()]
        input_data = self.get_table_data()

        for k, v in input_data.items():
            table_data.append([k] + v)

        t = []

        table = Table(table_data, repeatRows=1)

        # Установка шрифта и кодировки для таблицы
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),

            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))

        t.append(table)

        pdf.build(t)
        print("pdf сформирован")

    def get_table_data(self):
        main = Main()
        grid = Grid()
        command = Command()

        table_data = {}
        for i, player in enumerate(command.get_players()):
            row_values = []
            for j in range(1, len(grid.get_headers())):
                entry = grid.window.grid_slaves(row=i+1, column=j)[0]
                row_values.append(entry.get())
            table_data[player] = row_values
    
        return table_data
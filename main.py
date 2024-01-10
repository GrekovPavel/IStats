from tkinter import *
from tkinter import ttk
from app.Command import Command
from app.Grid import Grid
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from tkinter.messagebox import showerror, showwarning, showinfo

class Main:
    window = []

    def create_pdf(self):

        pdf_headers = ["Игрок", 
                        "Голы", 
                        "Ассисты", 
                        "Уд. в створ", 
                        "Уд. мимо", 
                        "Уд. заблок",  
                        "Потери", 
                        "Перехваты", 
                        "Отборы",
                        "Фолы",
                        "Фолы с.",
                        "ЖК",
                        "КК",
                        "Угловые",
                        "Пасы",
                        "Сейвы(вратарь)",
                        ]

        pdfmetrics.registerFont(TTFont('DejaVuSans', 'fonts/DejaVuSans.ttf'))

        pdf = SimpleDocTemplate("result.pdf", pagesize=letter)

        table_data = [pdf_headers]
        input_data = self.get_table_data()

        for k, v in input_data.items():
            table_data.append([k] + v)

        t = []

        table = Table(table_data, repeatRows=1)

        # Установка шрифта и кодировки для таблицы
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'DejaVuSans'),

            ('FONTSIZE', (0, 0), (-1, -1), 6),
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
        showinfo(title="Успешно", message="pdf сформирован")

    def get_table_data(self):
        command = Command()

        table_data = {}
        for i, player in enumerate(command.get_players()):
            row_values = []
            for j in range(1, len(Grid().get_headers())):
                entry = self.window.grid_slaves(row=i+1, column=j)[0]
                row_values.append(entry.get())
            table_data[player] = row_values
    
        return table_data

    def set_window(self):
        self.window = Tk()
        self.window.title("stats")    
        self.window.geometry("1000x500")
        self.window.option_add("*tearOff", FALSE)

    def set_menu(self):
        main_menu = Menu()
        
        command_menu = Menu()
        command_menu.add_command(label="Добавить игроков", command=Command().create_command)

        grid_menu = Menu()
        grid_menu.add_command(label="Сформировать таблицу", command=Grid(self.window).create_table)
        grid_menu.add_command(label="Сформировать PDF", command=self.create_pdf)

        main_menu.add_cascade(label="Команда", menu=command_menu)
        main_menu.add_cascade(label="Таблица", menu=grid_menu)

        self.window.config(menu=main_menu)

    def run_app(self):
        self.set_window()
        self.set_menu()
        self.window.mainloop()

if __name__ == "__main__":
    app = Main()
    app.run_app()

from tkinter import *
from tkinter import ttk
from app.Command import Command
from app.Grid import Grid
from app.Pdf import Pdf

class Main:
    window = []

    def set_window(self):
        self.window = Tk()
        self.window.title("stats")    
        self.window.geometry("1000x500")
        self.window.option_add("*tearOff", FALSE)
    
    def get_headers(self):
        return self.window

    def set_menu(self):
        main_menu = Menu()
        
        command_menu = Menu()
        command_menu.add_command(label="Добавить игроков", command=Command().create_command)

        grid_menu = Menu()
        grid_menu.add_command(label="Сформировать таблицу", command=Grid(self.window).create_table)
        grid_menu.add_command(label="Сформировать PDF", command=Pdf().create_pdf)

        main_menu.add_cascade(label="Команда", menu=command_menu)
        main_menu.add_cascade(label="Таблица", menu=grid_menu)

        self.window.config(menu=main_menu)

    def run_app(self):
        self.set_window()
        self.set_menu()
        self.window.mainloop()
        print(Grid().get_headers())

if __name__ == "__main__":
    app = Main()
    app.run_app()

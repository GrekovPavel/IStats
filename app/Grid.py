from tkinter import *
from app.Command import Command
from main import Main


class Grid:
    headers = []

    def __init__(self, window=None):
        self.window = window
        self.set_headers()
    
    def set_headers(self):
        self.headers = ["Игрок", 
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

    def get_headers(self):
        return self.headers
    
    def create_table(self): 
        main = Main()
        
        for i, header in enumerate(self.get_headers()):
            label = Label(self.window, text=header)
            label.grid(row=0, column=i)

        command = Command()
        players = command.get_players()

        for i, value in enumerate(players):
            label = Label(self.window, text=value)
            label.grid(row=i+1, column=0)

            for j in range(1, len(self.get_headers())):
                header = self.get_headers()[j]
                width = len(header)
                if width < 5:
                    width = 5
                entry = Entry(self.window, width=width)
                entry.grid(row=i+1, column=j)


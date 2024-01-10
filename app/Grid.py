from tkinter import *
from app.Command import Command
from main import Main


class Grid:
    headers = []

    def __init__(self, window=None):
        self.window = window
        self.set_headers()
    
    def set_headers(self):
        self.headers = ["Игрок", "Удары", "Голы", "Пасы"]

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
                entry = Entry(self.window)
                entry.grid(row=i+1, column=j)


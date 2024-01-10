from tkinter import *
from tkinter import ttk

class Command:
    players = []
    entryes = []

    def get_players(self):
        return self.players

    def add_players(self):
        self.players.clear()
        count = 1
        for entry in self.entryes:
            if entry.get() != "":
                self.players.append(str(count) + ". "+ entry.get())
                count += 1
        
    def create_command(self):
        command_window = Tk()
        command_window.title("Добавить игроков")    
        command_window.geometry("400x600")
        
        label = Label(command_window, text="Введите игроков") 
        label.pack()   

        self.entryes.clear()
        for i in range(18):
            entry = ttk.Entry(command_window)
            entry.pack(pady=3)
            self.entryes.append(entry)

        btn = ttk.Button(command_window, text="Добавить", command=self.add_players)
        btn.pack()

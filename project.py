import tkinter
import customtkinter

from datetime import datetime

class Habit():

    def __init__(self, name: str, days: list, start_date=None) -> None:
        self.name = name
        self.days = days
        self.streak = 0
        self.start_date = start_date or datetime.date.today()
        self.completed_today = False

    def mark_completed(self) -> None:
        self.compeleted_today = True
        self.streak += 1

    def mark_uncompleted(self) -> None:
        self.compeleted_today = False





def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    
    create_gui()

def create_gui() -> None:
    gui = customtkinter.CTk()
    gui.title("Habit Tracker")
    gui.geometry("800x600")

    label = tkinter.Label(gui, text="Habit Tracker", font=("Arial", 18))
    label.pack()

    gui.mainloop()

if __name__ == "__main__":
    main()
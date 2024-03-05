from tkinter import *
from tkinter import ttk

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
    create_gui()

def create_gui() -> None:
    gui = Tk()
    gui.title("Habit Tracker")
    gui.geometry("800x600")

    frame = ttk.Frame(gui, padding="3 3 12 12")
    frame.grid(column=0, row=0) 
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1)

    habit_label = ttk.Label(frame, text="Habit Tracker", font=("Arial", 18))
    habit_label.grid(column=0, row=0, columnspan=2, sticky=(N, W, E, S))

    day_label = ttk.Label(frame, text="Day", font=("Arial", 18))
    day_label.grid(column=0, row=1, columnspan=2)

    habit2_label = ttk.Label(frame, text="Habit", font=("Arial", 18))
    habit2_label.grid(column=0, row=2, columnspan=2, sticky=(N, W, E, S))

    checkbox_label = ttk.Label(frame, text="Check", font=("Arial", 18))
    checkbox_label.grid(column=1, row=2, columnspan=2)



    gui.mainloop()

if __name__ == "__main__":
    main()
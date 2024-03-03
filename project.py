import tkinter

from datetime import datetime

class Habit():

    def __init__(self, name, frequency, start_date=None) -> None:
        self.name = name
        self.frequency = frequency
        self.streak = 0
        self.start_date = start_date or datetime.date.today()
        self.completed_today = False
        self.notes = []

    def mark_completed(self) -> None:
        self.compeleted_today = True
        self.streak += 1

    def mark_uncompleted(self) -> None:
        self.compeleted_today = False

    def add_note(self, note: str) -> None:
        self.notes.append(note)




def main():
    create_gui()

def create_gui() -> None:
    gui = tkinter.Tk()
    gui.title("Habit Tracker")
    gui.geometry("800x600")

    label = tkinter.Label(gui, text="Habit Tracker", font=("Arial", 18))
    label.pack()

    gui.mainloop()

if __name__ == "__main__":
    main()
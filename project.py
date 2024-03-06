from tkinter import *
from tkinter import ttk

from datetime import date

class Habit():

    def __init__(self, name: str, days: list, start_date=None) -> None:
        self.name = name
        self.days = days
        self.streak = 0
        self.start_date = start_date or date.today()
        self.completed_today = False

    def mark_completed(self) -> None:
        self.compeleted_today = True
        self.streak += 1

    def mark_uncompleted(self) -> None:
        self.compeleted_today = False

habit_list = []

def main():
    create_gui()
    
def create_gui() -> None:
    gui = Tk()
    gui.title("Habit Tracker")

    frame = ttk.Frame(gui, padding="3 3 12 12")
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1)

    today = get_weekday()
    day_label = ttk.Label(frame, text=today, font=("Arial", 18))
    day_label.grid(column=0, row=0, columnspan=2)

    habit_label = ttk.Label(frame, text="Habit", font=("Arial", 18), padding=10)
    habit_label.grid(column=0, row=1)

    checkbox_label = ttk.Label(frame, text="Check", font=("Arial", 18), padding=10)
    checkbox_label.grid(column=1, row=1)

    button = ttk.Button(frame, text="Add Habit", command=add_habit_gui)
    button.grid(column=0, row=3, columnspan=2)
    
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)

    gui.mainloop()

def get_weekday() -> str:
    today = (str(date.today()).split("-"))
    today = [int(integer) for integer in today]
    today = date(*today).weekday()

    match today:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"


def add_habit_gui() -> None:
    habit_gui = Tk()
    habit_gui.title("Add Habit")

    frame = ttk.Frame(habit_gui, padding="3 3 12 12")
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 
    habit_gui.columnconfigure(0, weight=1) 
    habit_gui.rowconfigure(0, weight=1)

    global habit_name
    habit_name = StringVar()
    global habit_days
    habit_name = StringVar()


    label1 = ttk.Label(frame, text="Name", padding=10)
    label1.grid(column=0, row=0, columnspan=2)
    habit_entry = ttk.Entry(frame, textvariable=habit_name)
    habit_entry.grid(column=0, row=1, columnspan=2)

    
    dayslist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysvar = StringVar(value=dayslist)
    
    label2 = ttk.Label(frame, text="Days", padding=10)
    label2.grid(column=0, row=2, columnspan=2)
    days_list = Listbox(frame, listvariable=daysvar, height=7)
    days_list.grid(column=0, row=3, columnspan=2)



def create_habit():
    print(habit_name.get())


if __name__ == "__main__":
    main()
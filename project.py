from tkinter import *
from tkinter import ttk
from csv import DictWriter
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

    button = ttk.Button(frame, text="Add Habit", command=create_habit)
    button.grid(column=0, row=3, columnspan=2)
    

    global habit_name
    habit_name = StringVar()

    label1 = ttk.Label(frame, text="Name", padding=10)
    label1.grid(column=0, row=4, columnspan=2)
    habit_entry = ttk.Entry(frame, textvariable=habit_name)
    habit_entry.grid(column=0, row=5, columnspan=2)

    global days_list
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysvar = StringVar(value=days_list)

    label2 = ttk.Label(frame, text="Days", padding=10)
    label2.grid(column=0, row=6, columnspan=2)
    
    global days_listbox
    days_listbox = Listbox(frame, listvariable=daysvar, height=7, selectmode="extended")
    days_listbox.grid(column=0, row=7, columnspan=2)

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



def create_habit():
    try:
        index_days = days_listbox.curselection()
        days_selected  = [days_list[index_day] for index_day in index_days]
        days_selected = ",".join(days_selected)
        
        name = habit_name.get()
        habit = {"name": name, "days": days_selected, "streak": 0, "start_date": date.today()}
        
        with open("habits.csv", "a") as file:
            fieldnames = ["name", "days", "streak", "start_date"]
            writer = DictWriter(file, fieldnames=fieldnames)
            writer.writerow(habit)
    except: 
        pass



if __name__ == "__main__":
    main()
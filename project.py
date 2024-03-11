from tkinter import *
from tkinter import ttk
from csv import DictWriter, DictReader
from datetime import date
import pandas as pd

class Habit():

    @classmethod
    def update_habit(cls, object) -> None:
        df = pd.read_csv("habits.csv")
        df.loc[df["name"] == object.name, "streak"] = object.streak
        df.to_csv("habits.csv", index=False)

    def __init__(self, name: str, days: list, streak=0, start_date=None) -> None:
        self.name = name
        self.days = days
        self.streak = streak
        self.start_date = start_date or date.today()
        self.completed_today = False

    def mark_completed(self) -> None:
        self.compeleted_today = True
        self.streak = int(self.streak)
        self.streak += 1
        Habit.update_habit(self)

    def mark_uncompleted(self) -> None:
        self.compeleted_today = False







habits_objects_list = []
gui = 0

def main():
    get_habits()
    create_gui()


def create_gui() -> None:
    gui = Tk()
    gui.title("Habit Tracker")

    frame = ttk.Frame(gui, padding="20")
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1)

    today = get_weekday()
    day_label = ttk.Label(frame, text=today, font=("Arial", 18))
    day_label.grid(column=0, row=0, columnspan=2, pady=10)

    habit_label = ttk.Label(frame, text="Habit", font=("Arial", 18))
    habit_label.grid(column=0, row=1, padx=10)

    checkbox_label = ttk.Label(frame, text="Check", font=("Arial", 18))
    checkbox_label.grid(column=1, row=1, padx=10)

    z = 2

    for i, habit_object in enumerate(habits_objects_list):

        if today in habit_object.days:

            object_name = habit_object.name
            habit_name_label = ttk.Label(frame, text=object_name, font=("Arial", 12))
            habit_name_label.grid(column=0, row=i+2, padx=10, pady=5)

            checkbox = ttk.Checkbutton(frame, command=habit_object.mark_completed)
            checkbox.grid(column=1, row=i+2, padx=10, pady=5)

            z += 1

    button = ttk.Button(frame, text="Add Habit", command=create_habit)
    button.grid(column=0, row=z+1, columnspan=2, pady=10)

    global habit_name
    habit_name = StringVar()

    label1 = ttk.Label(frame, text="Name", padding=10)
    label1.grid(column=0, row=z+2, columnspan=2)

    habit_entry = ttk.Entry(frame, textvariable=habit_name)
    habit_entry.grid(column=0, row=z+3, columnspan=2, pady=5)

    global days_list
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysvar = StringVar(value=days_list)

    label2 = ttk.Label(frame, text="Days", padding=10)
    label2.grid(column=0, row=z+4, columnspan=2)

    global days_listbox
    days_listbox = Listbox(frame, listvariable=daysvar, height=7, selectmode="extended")
    days_listbox.grid(column=0, row=z+5, columnspan=2, pady=5)

    for i in range(len(habits_objects_list) + 7):
        frame.rowconfigure(i, weight=1)

    for i in range(2):
        frame.columnconfigure(i, weight=1)


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



def create_habit() -> None:
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
    
    get_habits()


def get_habits() -> None:
    try:
        habit_details_list = []

        with open("habits.csv") as file:

            fieldnames = ["name", "days", "streak", "start_date"]
            reader = DictReader(file, fieldnames=fieldnames)
            next(reader)
            for row in reader:
                habit_details_list.append(row)
        
        for item in habit_details_list:
            habits_objects_list.append(Habit(**item))


    except:
        pass 

    if gui:
        gui.update()


if __name__ == "__main__":
    main()
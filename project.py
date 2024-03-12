from tkinter import *
from tkinter import ttk
from csv import DictWriter, DictReader
from datetime import date
import pandas as pd
from customtkinter import *


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
        self.completed_today = BooleanVar(value=False)

    def check(self):
        if self.completed_today.get() == 1:
            self.streak = int(self.streak)
            self.streak += 1
            Habit.update_habit(self)

        elif self.completed_today.get() == 0:
            self.streak = int(self.streak)
            self.streak -= 1
            Habit.update_habit(self)


habits_objects_list = []
gui = CTk()
gui.title("Habit Tracker")
gui.geometry("800x800")  # Set window size using geometry
set_appearance_mode("dark")  # Use dark theme


def main():
    get_habits()
    create_gui()


def create_gui() -> None:

    # Main frame with rounded corners
    frame = CTkFrame(master=gui, corner_radius=10)
    frame.grid(column=0, row=0, sticky="nsew")

    gui.grid_columnconfigure(0, weight=1)
    gui.grid_rowconfigure(0, weight=1)

    # Today's label
    today = get_weekday()
    day_label = CTkLabel(master=frame, text=today, font=("Arial", 16))
    day_label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

    # Habit and Checkbox labels
    habit_label = CTkLabel(master=frame, text="Habit", font=("Arial", 14))
    habit_label.grid(column=0, row=1, padx=10, pady=5)

    checkbox_label = CTkLabel(master=frame, text="Check", font=("Arial", 14))
    checkbox_label.grid(column=1, row=1, padx=10, pady=5)

    row_counter = 2  # Track the current row for habit entries

    # Iterate through habits and display them with checkboxes
    for i, object in enumerate(habits_objects_list):
        if today in object.days:
            object_name = object.name

            habit_name_label = CTkLabel(master=frame, text=object_name, font=("Arial", 14))
            habit_name_label.grid(column=0, row=row_counter, padx=10, pady=5)

            checkbox = CTkCheckBox(
                master=frame,
                text="",  # Consider adding checkbox text for clarity
                onvalue=1,
                offvalue=0,
                variable=object.completed_today,
                command=object.check,
            )
            checkbox.grid(column=1, row=row_counter, padx=10, pady=5)

            row_counter += 1  # Increment row for the next habit

    # Buttons with custom styles
    add_habit_button = CTkButton(master=frame, text="Add Habit", command=add_habit_gui)
    add_habit_button.configure(width=200, height=40, fg_color="#ffffff", hover_color="#2a2a2a")
    add_habit_button.grid(column=0, row=row_counter, columnspan=2, padx=10, pady=10)

    details_button = CTkButton(master=frame, text="Habit Details", command=habit_details_gui)
    details_button.configure(width=200, height=40, fg_color="#ffffff", hover_color="#2a2a2a")
    details_button.grid(column=0, row=row_counter + 1, columnspan=2, padx=10, pady=10)

    # Adjust row weights for dynamic content
    for i in range(row_counter + 2):
        frame.rowconfigure(i, weight=1)

    # Adjust column weights for equal spacing
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

def add_habit_gui() -> None:

    top = Toplevel(gui)
    top.title("Add Habit")

    frame = ttk.Frame(top, padding="20", style="TFrame")
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 

    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)

    global habit_name
    habit_name = StringVar()

    label1 = ttk.Label(frame, text="Name", padding=10, style='TLabel')
    label1.grid(column=0, row=0, columnspan=2)

    habit_entry = ttk.Entry(frame, textvariable=habit_name)
    habit_entry.grid(column=0, row=1, columnspan=2, pady=5)

    global days_list
    days_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    daysvar = StringVar(value=days_list)

    label2 = ttk.Label(frame, text="Days", padding=10, style='TLabel')
    label2.grid(column=0, row=2, columnspan=2)

    global days_listbox
    days_listbox = Listbox(frame, listvariable=daysvar, height=7, selectmode="extended")
    days_listbox.grid(column=0, row=3, columnspan=2, pady=5)

    button = ttk.Button(frame, text="Add Habit", command=create_habit, style='TButton')
    button.grid(column=0, row=4, columnspan=2, pady=10)

    for i in range(4):
        frame.rowconfigure(i, weight=1)

    for i in range(1):
        frame.columnconfigure(i, weight=1)


def habit_details_gui() -> None:

    top = Toplevel(gui)
    top.title("Add Habit")

    frame = ttk.Frame(top, padding="20", style="TFrame")
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 

    top.columnconfigure(0, weight=1)
    top.rowconfigure(0, weight=1)

    label_1 = ttk.Label(frame, text="Habit Name", padding=10, style="TLabel")
    label_2 = ttk.Label(frame, text="Days", padding=10, style="TLabel")
    label_3 = ttk.Label(frame, text="Streak", padding=10, style="TLabel")
    label_4 = ttk.Label(frame, text="Start Date", padding=10, style="TLabel")

    label_1.grid(column=0, row=0)
    label_2.grid(column=1, row=0)
    label_3.grid(column=2, row=0)
    label_4.grid(column=3, row=0)

    z = 1

    for i, habit in enumerate(habits_objects_list):
        label_name = ttk.Label(frame, text=habit.name, padding=10, style="TLabel")
        label_days = ttk.Label(frame, text=habit.days, padding=10, style="TLabel")
        label_streak = ttk.Label(frame, text=habit.streak, padding=10, style="TLabel")
        label_start = ttk.Label(frame, text=habit.start_date, padding=10, style="TLabel")

        label_name.grid(column=0, row=i+1)
        label_days.grid(column=1, row=i+1)
        label_streak.grid(column=2, row=i+1)
        label_start.grid(column=3, row=i+1)

        z += 1

    for i in range(z):
        frame.rowconfigure(i, weight=1)

    for i in range(4):
        frame.columnconfigure(i, weight=1)



if __name__ == "__main__":
    main()
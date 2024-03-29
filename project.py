from tkinter import *
from tkinter import ttk, messagebox
from csv import DictWriter, DictReader
from datetime import date
import pandas as pd
import random
from colorlist import colors

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

    def check(self) -> None:
        if self.completed_today.get() == 1:
            self.streak = int(self.streak)
            self.streak += 1
            Habit.update_habit(self)

        elif self.completed_today.get() == 0:
            self.streak = int(self.streak)
            self.streak -= 1
            Habit.update_habit(self)

def generate_random_color() -> tuple:
    return random.choice(colors)

habits_objects_list = []
gui = Tk()
gui.title("Habit Tracker")
gui.minsize(800, 800)
gui.option_add('*tearOff', FALSE)

style = ttk.Style()
color = generate_random_color()
style.configure('TFrame', background=color)
style.configure('Day.TLabel', background=color, font=("Courier", 40), foreground=generate_random_color())
style.configure('TLabel', background=color, font=('Arial', 12))
style.configure('TButton', background='#4caf50', foreground='#ffffff', font=('Arial', 12))


def main():
    get_habits()
    create_gui()


def create_gui() -> None:

    frame = ttk.Frame(gui, padding="20", style='TFrame')
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 
    gui.columnconfigure(0, weight=1)
    gui.rowconfigure(0, weight=1)

    today = get_weekday()
    day_label = ttk.Label(frame, text=today, style='Day.TLabel')
    day_label.grid(column=0, row=0, columnspan=2, pady=10)


    z = 1

    for i, object in enumerate(habits_objects_list):

        if today in object.days:
            object_name = object.name

            color = generate_random_color()
            style.configure('Habit.TFrame', background=color)
            habit_frame = ttk.Frame(frame, style="Habit.TFrame")
            habit_frame.grid(column=0, columnspan=2, row=z)

            style.configure('Habit.TLabel', background=color, font=('Arial', 20))
            habit_name_label = ttk.Label(habit_frame, text=object_name, style="Habit.TLabel")
            habit_name_label.grid(column=0, row=0, padx=20, pady=5)

            style.configure('TCheckbutton', background=color, size=30)
            checkbox = ttk.Checkbutton(habit_frame, onvalue=1, offvalue=0, variable=object.completed_today, command=object.check)
            checkbox.grid(column=1, row=0, padx=20, pady=5)

            z += 1

    button = ttk.Button(frame, text="Add Habit", command=add_habit_gui, style='TButton')
    button.grid(column=0, row=z, pady=10)

    style.configure('Details.TButton', background=generate_random_color(), foreground="black", font=('Arial', 12))
    button2 = ttk.Button(frame, text="Habit Details", command=habit_details_gui, style="Details.TButton")
    button2.grid(column=1, row=z, pady=5)

    menubar = Menu(gui)
    gui.config(menu=menubar)

    menubar.add_command(label="Delete Habit", command=delete_habit_gui)

    for i in range(z+3):
        frame.rowconfigure(i, weight=1)

    for i in range(2):
        frame.columnconfigure(i, weight=1)

    gui.mainloop()

def get_weekday(**test) -> str:
    today = (str(date.today()).split("-"))
    if test:
        today = test["date"]
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



def create_habit(**test) -> None: # Returns Errors if wrong
    try:
        if not test:
            index_days = days_listbox.curselection()
            if not index_days:
                raise IndexError
            
            days_selected  = [days_list[index_day] for index_day in index_days]
            days_selected = ",".join(days_selected)

            name = habit_name.get()
            if not name:
                raise NameError
            
            habit = {"name": name, "days": days_selected, "streak": 0, "start_date": date.today()}
        
        elif test:
            if not test["name"]:
                raise NameError
            if not test["days"]:
                raise IndexError
            
            habit = {"name": test["name"], "days": test["days"], "streak": 0, "start_date": date.today()}
            with open("test_habits.csv", "a") as file:
                fieldnames = ["name", "days", "streak", "start_date"]
                writer = DictWriter(file, fieldnames=fieldnames)
                writer.writerow(habit)

        if not test:
            with open("habits.csv", "a") as file:
                fieldnames = ["name", "days", "streak", "start_date"]
                writer = DictWriter(file, fieldnames=fieldnames)
                writer.writerow(habit)

            habit_entry.delete("0", "end")
            days_listbox.selection_clear("0", "end")
            messagebox.showinfo(message="Habit Added Succesfully")

    except NameError:
        if not test:
            messagebox.showinfo(message="Please add a Name!")
        return NameError
        
    except IndexError:
        if not test:
            messagebox.showinfo(message="Please Choose a Day!")
        return IndexError
    except: 
        pass

    if not test:
        get_habits()
        create_gui()


def get_habits(**test) -> None:
    global habits_objects_list
    if habits_objects_list:
        habits_objects_list = []
    try:
        habit_details_list = []

        if not test:
            with open("habits.csv") as file:
        
                fieldnames = ["name", "days", "streak", "start_date"]
                reader = DictReader(file, fieldnames=fieldnames)
                next(reader)
                for row in reader:
                    habit_details_list.append(row)

        elif test:
            with open("test_habits.csv") as file:
            
                fieldnames = ["name", "days", "streak", "start_date"]
                reader = DictReader(file, fieldnames=fieldnames)
                next(reader)
                for row in reader:
                    habit_details_list.append(row)
        
        for item in habit_details_list:
            habits_objects_list.append(Habit(**item))


    except:
        pass 


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

    global habit_entry
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

def delete_habit_gui() -> None:
    delete_gui = Toplevel(gui)
    delete_gui.title("Delete Habit")

    frame = ttk.Frame(delete_gui, padding="20", style="TFrame")
    frame.grid(column=0, row=0, sticky=(N, S, E, W)) 

    style.configure('TLabel', background="white", font=('Arial', 12))
    label1 = ttk.Label(frame, text="Name of Habit to Delete", padding=10, style='TLabel')
    label1.grid(column=0, row=0, columnspan=2)

    global delete_name
    delete_name = StringVar()

    global delete_entry
    delete_entry = ttk.Entry(frame, textvariable=delete_name)
    delete_entry.grid(column=0, row=1, columnspan=2, pady=5)

    style.configure('Delete.TButton', background="red", foreground='#ffffff', font=('Arial', 12))
    button = ttk.Button(frame, text="Delete Habit", command=delete_habit, style='Delete.TButton')
    button.grid(column=0, row=2, columnspan=2, pady=10)
    

def delete_habit(**test) -> None: # Returns Errors if Wrong
    confirm = 0
    if not test:
        style.configure('TLabel', font=('Arial', 12))
        confirm = messagebox.askyesno(message="Are you sure you want to delete this Habit?", icon='question', title="confirmation")
    if confirm or test:
        try:
            row = None
            if not test:
                df = pd.read_csv("habits.csv")
                row = df[df["name"] == delete_name.get()]

            elif test:
                df = pd.read_csv("test_habits.csv")
                row = df[df["name"] == test["name"]]

            if not row.empty:
            
                index = row.index
                
                df = df.drop(index)

                if not test:
                    df.to_csv("habits.csv", index=False)
                    messagebox.showinfo(message="Habit Deleted")
                    get_habits()
                    create_gui()
                
                if test:
                    df.to_csv("test_habits.csv", index=False)

            elif row.empty:
                raise LookupError

        except LookupError:
            if not test:
                messagebox.showinfo(message="Unable to find Habit")
            return LookupError
    else:
        pass

if __name__ == "__main__":
    main()
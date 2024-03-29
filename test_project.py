import pytest
from project import Habit, get_weekday, create_habit, delete_habit, get_habits, habits_objects_list
from datetime import date
import pandas as pd

@pytest.fixture
def habit():
    return Habit("Exercise", ["Monday", "Wednesday", "Friday"], streak=3)

def test_increase_streak(habit):
    habit.completed_today.set(1)
    habit.check()
    assert habit.streak == 4

def test_decrease_streak(habit):
    habit.completed_today.set(0)
    habit.check()
    assert habit.streak == 2

def test_create_habit():
    create_habit(name="Swimming", days="Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday") 
    create_habit(name='Reading', days='Sunday,Tuesday,Thursday,Saturday')
    create_habit(name='Running', days='Tuesday') 

    df = pd.read_csv("test_habits.csv")
    row = df[df["name"] == "Swimming"][["name", "days"]].iloc[0]
    row = f'{row["name"]},{row["days"]}'
    assert row == f'Swimming,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday'

    df = pd.read_csv("test_habits.csv")
    row = df[df["name"] == "Reading"][["name", "days"]].iloc[0]
    row = f'{row["name"]},{row["days"]}'
    assert row == f'Reading,Sunday,Tuesday,Thursday,Saturday'

    df = pd.read_csv("test_habits.csv")
    row = df[df["name"] == "Running"][["name", "days"]].iloc[0]
    row = f'{row["name"]},{row["days"]}'
    assert row == f'Running,Tuesday'

    assert create_habit(name="", days="Sunday") == NameError
    assert create_habit(name="Working Out", days="") == IndexError


def test_get_habits():
    get_habits(test=True)
    assert len(habits_objects_list) == 3

def test_delete_habit():
    delete_habit(name="Swimming")
    delete_habit(name="Reading")
    delete_habit(name="Running")

    df = pd.read_csv("test_habits.csv")
    row = df[df["name"] == "Swimming"][["name", "days"]]
    assert row.empty == True

    df = pd.read_csv("test_habits.csv")
    row = df[df["name"] == "Reading"][["name", "days"]]
    assert row.empty == True

    df = pd.read_csv("test_habits.csv")
    row = df[df["name"] == "Running"][["name", "days"]]
    assert row.empty == True

    assert delete_habit(name="Working") == LookupError


def test_get_weekday():
    assert get_weekday(date = ["2024", "03","19"]) == "Tuesday"
    assert get_weekday(date = ["2024", "01","10"]) == "Wednesday"
    assert get_weekday(date = ["2023", "12","25"]) == "Monday"
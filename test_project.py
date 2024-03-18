import pytest
from project import Habit, get_weekday

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

def test_get_weekday():
    today = get_weekday()
    .....


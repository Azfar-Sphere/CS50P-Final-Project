  # Habit Tracker
  ### Video Demo:  <URL HERE>
  ### Description
  Upon opening the project.py file, the user is introduced to the Habit class declaration. This class initializes habit objects, storing their details and handling functions such as updating habits.

The main function orchestrates the process, primarily comprising two functions:

get_habits(): Retrieves previously stored habits from a CSV file, creating Habit objects for each habit and storing them in the habits_objects_list to ensure persistence across program runs.
create_gui(): Constructs the GUI, displaying habits to be done for the current day. It utilizes the get_weekday() function to determine the current weekday and dynamically creates GUI elements based on stored habit data.
The create_habit() function facilitates habit addition by capturing user input, validating it, and storing the habit in the CSV file. If invoked without arguments, it interacts with the GUI elements. Conversely, when invoked with test arguments, it performs batch testing.

Similarly, functions like add_habit_gui(), habit_details_gui(), and delete_habit_gui() create GUI elements for adding habits, displaying habit details, and deleting habits, respectively.

Detailed Functionality:
create_gui(): Dynamically creates GUI elements based on stored habit data for the current day.
get_weekday(): Determines the current weekday using the date module.
create_habit(): Handles habit addition, fetching habit name and days from GUI elements or test arguments and storing them in the CSV file.
get_habits(): Retrieves previously stored habits from CSV files, creating Habit objects for each habit.
add_habit_gui(): Creates a pop-up GUI for adding a habit.
habit_details_gui(): Creates a GUI to display habit details.
delete_habit_gui(): Creates a GUI for deleting a habit.
delete_habit(): Handles habit deletion by prompting for confirmation, fetching habit details, and updating the CSV file.

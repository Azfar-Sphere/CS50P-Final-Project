  # Habit Tracker
  ### Video Demo:  <URL HERE>
  ### Description:
The decision to create a habit tracker stemmed from my personal experience with using a paper-based habit tracker. While effective, I found it more convenient to use a digital platform for better accessibility and ease of use.

I aimed for simplicity and vibrancy in the design, opting for a clean and straightforward interface that prioritizes functionality. One unique aspect is the random selection of background and button colors each time the habit tracker is launched, with the "generate_random_color" function picking a random color from a HUGE list of colors, enhancing its visual appeal and keeping the interface dynamic and refreshing.

  Upon opening the project.py file, the user is introduced to the Habit class declaration. This class initializes habit objects, storing their details and handling functions such as updating habits.

The main function orchestrates the process, primarily comprising two functions:

get_habits(): Retrieves previously stored habits from a CSV file, creating Habit objects for each habit and storing them in the habits_objects_list to ensure persistence across program runs.

create_gui(): Constructs the GUI, displaying habits to be done for the current day. It utilizes the get_weekday() function to determine the current weekday and dynamically creates GUI elements based on stored habit data.

The create_habit() function facilitates habit addition by capturing user input, validating it, and storing the habit in the CSV file. If invoked without arguments, it interacts with the GUI elements. Conversely, when invoked with test arguments, it performs batch testing.

Similarly, functions like add_habit_gui(), habit_details_gui(), and delete_habit_gui() create GUI elements for adding habits, displaying habit details, and deleting habits, respectively.

#### Detailed Functionality:

create_gui(): Dynamically creates GUI elements based on stored habit data for the current day.

get_weekday(): Determines the current weekday using the date module.

create_habit(): Handles habit addition, fetching habit name and days from GUI elements or test arguments and storing them in the CSV file.

get_habits(): Retrieves previously stored habits from CSV files, creating Habit objects for each habit.

add_habit_gui(): Creates a pop-up GUI for adding a habit.

habit_details_gui(): Creates a GUI to display habit details.

delete_habit_gui(): Creates a GUI for deleting a habit.

delete_habit(): Handles habit deletion by prompting for confirmation, fetching habit details, and updating the CSV file.

### Testing:

Some functions in the codebase include an optional argument named test. This feature enables the passing of custom arguments to functions directly from the file test_project.py. Typically, functions interact with variables obtained from GUI elements. However, **test serves as a backdoor for testing functions independently of the GUI. This capability eliminates the necessity of fetching values from entry boxes or list boxes during testing, streamlining the testing process.

The test_project.py file initiates by creating a fixture, a habit object, utilized in subsequent tests. It comprehensively tests instance functions within the Habit class and other relevant functions. Moreover, a testing csv file known as test_habits.csv is used to ensure the correct writing and deletion of values from the csv file. This ensures that the csv file used by the program, "habits.csv", remains unaffected by testing.

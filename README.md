  # Habit Tracker
    ### Video Demo:  <URL HERE>
    ### Description:
    Hi! What I wanted to make was a habit tracker app in python and I did just that! Using tkinter in python for my GUI, 
    I created a very simple and very colorful habit tracker that you can add your habits for each day. 
    The color of the gui and the buttons are also random and can be any one from the colors in the colorlist.py file.
    #### Functionality:
    When you open the project.py file, you'll be greeted first by the declaration of the Habit Class. 
    This class intializes the Habit Objects, stores its details and handles other functionality such
    as updating the habit.

    The main function is really simple! It is only two lines of code, calling the get_habits function,
    which retrieves all the habits preivously stored in the CSV file. Then, the create_gui function
    draws the gui.

    But, what does each function do? 

    The create_gui function gets the current weekday from the get_weekday function,
    then using the habits in the habit_objects_list, it creates the GUI with the 
    habits to do for today.

    The get_weekday function uses the date module to figure out which day it is.

    The create_habit function uses the entrybox in the habit gui to retrieve the habit name
    and then create the habit and store it in a csv file.

    The get_habits function retrieves all the previously stored habits in the csv file, creates Habit Objects
    for all said habits and then stores them in the habit_objects_list every time the program is run. This ensure
    all previously added habits are fetched.

    The add_habit_gui creates the popup gui that is used to add a habit. 

    Similarly, the habit_details_gui creates the gui to display the details of each habit.

    Similarly aswell, the delete_habit_gui creates the gui to delete a habit.

    The delete_habit function takes in the name of the habit entered in the delete habit GUI and deletes
    the habit from the CSV permanently.

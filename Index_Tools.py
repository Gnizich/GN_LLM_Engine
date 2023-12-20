import tkinter as tk
from tkinter import ttk
#import Build_Index as bi
import Build_Index2 as bi  #import AskBuild, AskQuestion

# Global variable to store the selected action
action_choice = None
action_dropdown = None
topic_choice = None
topic_dropdown = None
topic = ""
action = ""

# Function to initialize the main window
def create_main_window():
    global action_dropdown  # Declare action_dropdown as global
    global topic_dropdown  # Declare topic_dropdown as global

    # Create the main window
    window = tk.Tk()
    window.title("Python Tkinter Example")

    # Create the first row with dropdowns
    tk.Label(window, text="Topic").grid(row=0, column=0, padx=10, pady=10)
    topic_options = ["Select","Personal AI", "AI Tools"]
    topic_dropdown = ttk.Combobox(window, values=topic_options)
    topic_dropdown.grid(row=0, column=1, padx=10, pady=10)
    topic_dropdown.set("Select")

    tk.Label(window, text="Action").grid(row=0, column=2, padx=10, pady=10)
    action_options = ["Select", "Ask question", "Build index"]
    action_dropdown = ttk.Combobox(window, values=action_options)
    action_dropdown.grid(row=0, column=3, padx=10, pady=10)
    action_dropdown.set("Select")

    # Create the second row with buttons
    btn1 = tk.Button(window, text="Submit Instructions", command = Submit_Instructions)
    btn1.grid(row=1, column=0, padx=10, pady=10)

    btn2 = tk.Button(window, text="Button 2")
    btn2.grid(row=1, column=1, padx=10, pady=10)

    btn3 = tk.Button(window, text="Button 3")
    btn3.grid(row=1, column=2, padx=10, pady=10)

    # Create the text boxes
    tk.Label(window, text="Question").grid(row=2, column=0, columnspan=4)
    question_text = tk.Text(window, width=70, height=10)
    question_text.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    tk.Label(window, text="Response").grid(row=4, column=0, columnspan=4)
    response_text = tk.Text(window, width=70, height=10)
    response_text.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    return window

def Submit_Instructions():
    global action_choice
    global topic_choice
    global topic
    global action

    action_choice = action_dropdown.get()
    topic_choice = topic_dropdown.get()

    if topic_choice == "Personal AI":
        topic = "gn"
    elif topic_choice == "AI Tools":
        topic = "ai"
    else:
        print("Invalid topic selected")

    if action_choice == "Build index":
        action = "build"
    elif action_choice == "Ask question":
        action = "ask"
    else:
        print("Invalid action selected")

    print("Current Action Choice:", action_choice)  # Optional, for demonstration
    print("Current Topic Choice:", topic_choice)

    if topic_choice != 'Select' and action_choice != 'Select':
        if action_choice == "Build index":
            bi.AskBuild(topic, action)
            print('Called ask/build function')
        elif action_choice == 'Ask question':
            bi.AskQuestion(topic, action)
            print('Call ask question function')
    else:
        print("Select is not a valid dropdown choice!")

# Create and run the window
main_window = create_main_window()
main_window.mainloop()

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

def on_closing():
    root.destroy()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

def create_widgets(window):

    font_style = ("Arial", 24)
    bigfont = tkFont.Font(family="Helvetica",size=18)
    root.option_add("*TCombobox*Listbox*Font", bigfont)
    root.option_add("*Font", bigfont)

    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    style = ttk.Style()
    style.configure('TCombobox', font=font_style)

    topic_dropdown = ttk.Combobox(window, font=font_style, style='TCombobox')
    action_dropdown = ttk.Combobox(window, font=font_style, style='TCombobox')

    topic_label = tk.Label(window, text="Topic", font=font_style)
    topic_label.place(x=20, y=20)

    topic_dropdown = ttk.Combobox(window, style='TCombobox', width=30)
    topic_dropdown['values'] = ('Select', 'Personal AI', 'AI Tools')
    topic_dropdown.current(0)
    topic_dropdown.place(x=300, y=20)

    action_label = tk.Label(window, text="Action", font=font_style)
    action_label.place(x=750, y=20)

    action_dropdown = ttk.Combobox(window, style='TCombobox', width=30)
    action_dropdown['values'] = ('Select', 'Build index', 'Ask question')
    action_dropdown.current(0)
    action_dropdown.place(x=900, y=20)

    # Create submit button
    submit_button = tk.Button(text="Go", bg="blue", fg="white", command=Submit_Instructions)

    # Position and size the button
    submit_button.place(x=150, y=100, width=100, height=30)


    question_label = tk.Label(window, text="Question", font=font_style)
    question_label.place(x=20, y=200)

    question_text = tk.Text(window, height=10, font=font_style)
    question_text.place(x=20, y=260, width=1300, height=200)

    response_label = tk.Label(window, text="Response", font=font_style)
    response_label.place(x=20, y=500)

    response_text = tk.Text(window, height=5, font=font_style)
    response_text.place(x=20, y=560, width=1300, height=200)
def create_main_window():

    global root

    root = tk.Tk()
    root.geometry("1500x800")

    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=0)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)

    PADX = 10
    PADY = 5

    FONT = ("Helvetica", 32)

    create_widgets(root)

    root.protocol("WM_DELETE_WINDOW", on_closing)

    return root

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

main_window = create_main_window()
main_window.mainloop()

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import Build_Index as bi  # Assuming this contains the AskQuestion function

def on_closing():
    root.destroy()

WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 800

# Declare global variables for dropdowns and text widgets
global topic_dropdown, action_dropdown, question_text, response_text

def create_widgets(window):
    global action_dropdown, topic_dropdown, question_text, response_text

    font_style = ("Arial", 24)
    bigfont = tkFont.Font(family="Helvetica", size=18)
    window.option_add("*TCombobox*Listbox*Font", bigfont)
    window.option_add("*Font", bigfont)

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

    submit_button = tk.Button(window, text="Go", bg="blue", fg="white", command=Submit_Instructions)
    submit_button.place(x=150, y=410, width=100, height=30)

    question_label = tk.Label(window, text="Question", font=font_style)
    question_label.place(x=20, y=100)

    question_frame = tk.Frame(window)  # Frame to hold text widget and scrollbar
    question_frame.place(x=20, y=160, width=1300, height=200)

    question_text = tk.Text(question_frame, height=10, font=font_style)
    question_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    question_scroll = tk.Scrollbar(question_frame, command=question_text.yview)
    question_text['yscrollcommand'] = question_scroll.set
    question_scroll.pack(side=tk.RIGHT, fill=tk.Y)

    response_label = tk.Label(window, text="Response", font=font_style)
    response_label.place(x=20, y=500)

    response_frame = tk.Frame(window)  # Frame to hold text widget and scrollbar
    response_frame.place(x=20, y=560, width=1300, height=200)

    response_text = tk.Text(response_frame, height=5, font=font_style)
    response_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    response_scroll = tk.Scrollbar(response_frame, command=response_text.yview)
    response_text['yscrollcommand'] = response_scroll.set
    response_scroll.pack(side=tk.RIGHT, fill=tk.Y)

def submit_instructions():
    global action_choice, topic_choice, topic, action

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

    print("Current Action Choice:", action_choice)  # For debugging
    print("Current Topic Choice:", topic_choice)  # For debugging

    if topic_choice != 'Select' and action_choice != 'Select':
        if action_choice == "Build index":
            bi.AskBuild(topic, action)
            print('Called ask/build function')
        elif action_choice == 'Ask question':
            question = question_text.get("1.0", tk.END).strip()  # Get question
            response = bi.AskQuestion(topic, action, question)  # Get response from AskQuestion
            response_text.delete("1.0", tk.END)  # Clear response textbox
            response_text.insert(tk.END, response)  # Display response
            print(response)
    else:
        print("Select is not a valid dropdown choice!")

def Submit_Instructions():
    submit_instructions()

def create_main_window():
    global root

    root = tk.Tk()
    root.geometry("1500x800")

    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=0)
    root.rowconfigure(2, weight=1)
    root.columnconfigure(0, weight=1)

    create_widgets(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)

    return root

main_window = create_main_window()
main_window.mainloop()

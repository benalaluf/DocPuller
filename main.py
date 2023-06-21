import tkinter as tk
from tkinter import ttk
from tkinter import *

from tkcalendar import Calendar, DateEntry


def on_generate_click():
    entry_text = entry.get()
    check_state = checkbox_var.get()

    print("Entry text:", entry_text)
    print("Checkbox state:", check_state)
    print('Date', cal.get_date())


# Create the main window
window = tk.Tk()
window.title("docPuller")
window.geometry("800x800")
# Create a frame for the input fields and checkbox


title_lable = ttk.Label(window, text="docPuller", font=('Arial', 50))
title_lable.pack(side='top', pady=10)

input_frame = ttk.Frame(window)
input_frame.pack(anchor='nw')

date_label = ttk.Label(input_frame, text="Date Field:")
date_label.grid(row=0, column=0,)

date_label = ttk.Label(input_frame, text="from:")
date_label.grid(row=1, column=0)
cal = DateEntry(input_frame, width=5, bg="darkblue", fg="white", year=2022)
cal.grid(row=1, column=1,)

date_label = ttk.Label(input_frame, text="to:")
date_label.grid(row=1, column=2,)
date_to = DateEntry(input_frame, width=5, bg="darkblue", fg="white", year=2023)
cal.grid(row=1, column=3,)

# Create an input field
entry_label = ttk.Label(input_frame, text="Input Field:")
entry_label.grid(row=2, column=0, sticky=(tk.W, tk.E))
entry = ttk.Entry(input_frame)
entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

# Create a checkbox
checkbox_var = tk.BooleanVar()
checkbox = ttk.Checkbutton(input_frame, text="Checkbox", variable=checkbox_var)
checkbox.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

# Create a big generate button
generate_button = tk.Button(window, text="Generate",height=5,width=30, command=on_generate_click)
generate_button.pack(side='bottom', pady=30)

# Run the main loop
window.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
def submit():
    selected_from_date = from_date_entry.get_date().strftime("%d/%m/%Y")
    selected_to_date = to_date_entry.get_date().strftime("%d/%m/%Y")
    selected_checkboxes = [var1.get(), var4.get()]  # Adjusted to include var1 and var4 only
    keywords = keyword_entry.get("1.0", tk.END).strip()

    messagebox.showinfo("Form Data",
                        f"From Date: {selected_from_date}\n"
                        f"To Date: {selected_to_date}\n"
                        f"Selected Checkboxes: {selected_checkboxes}\n"
                        f"Keywords: {keywords}")

# Create the main window
window = tk.Tk()
window.title("docPuller")

background_image = Image.open("real/background.jpeg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Headline
headline = tk.Label(window, text="docPuller", font=("Arial", 16, "bold"))
headline.pack(pady=10)

# Section 1: Date Selection
section1 = tk.Frame(window)
section1.pack(pady=10)

from_date_label = tk.Label(section1, text="From:")
from_date_label.pack(side="left")

from_date_entry = DateEntry(section1, date_pattern="dd/mm/yy", show_weeknumbers=False)
from_date_entry.pack(side="left")

to_date_label = tk.Label(section1, text="To:")
to_date_label.pack(side="left")

to_date_entry = DateEntry(section1, date_pattern="dd/mm/yy", show_weeknumbers=False)
to_date_entry.pack(side="left")

# Section 2: Checkboxes
section2 = tk.Frame(window)
section2.pack(pady=10)

checkbox_label = tk.Label(section2, text="File Types")
checkbox_label.pack()

var1 = tk.BooleanVar()
check1 = tk.Checkbutton(section2, text="Checkbox 1", variable=var1)
check1.pack(side="left")

var4 = tk.BooleanVar()
check4 = tk.Checkbutton(section2, text="Checkbox 4", variable=var4)
check4.pack(side="left")

# Section 3: Free Text Entry
section3 = tk.Frame(window)
section3.pack(pady=10)

keyword_label = tk.Label(section3, text="Keywords")
keyword_label.pack()

keyword_entry = tk.Text(section3, height=5, width=30)
keyword_entry.pack()

# Section 4: Submit Button
section4 = tk.Frame(window)
section4.pack(pady=10)

submit_button = tk.Button(section4, text="Submit", command=submit)
submit_button.pack()

# Start the main event loop
window.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk

last_count_of_directories = 0
last_count_of_keywords = 0
entrys_width = 40


def submit():
    selected_from_date = from_date_entry.get_date().strftime("%d-%m-%Y")
    selected_to_date = to_date_entry.get_date().strftime("%d-%m-%Y")
    selected_radio = radio_var.get()
    keywords = keyword_entry.get("1.0", tk.END).strip()
    selected_directories = [dir.strip() for dir in directory_entry.get("1.0", tk.END).split(",") if dir.strip()]

    messagebox.showinfo("Form Data",
                        f"Selected Directories: {', '.join(selected_directories)}\n"
                        f"From Date: {selected_from_date}\n"
                        f"To Date: {selected_to_date}\n"
                        f"Selected Radio: {selected_radio}\n"
                        f"Keywords: {keywords}")


def update_selected_directories(event):
    text = directory_entry.get("1.0", tk.END).strip()
    global last_count_of_directories
    if text.count(',') != last_count_of_directories or text.count(',') < 1:
        last_count_of_directories = text.count(',')
        selected_directories = text.split(',')
        selected_directory_label.config(text=f"Selected: {''.join(selected_directories)}")


def update_selected_keywords(event):
    text = keyword_entry.get("1.0", tk.END).strip()
    global last_count_of_keywords
    if text.count(',') != last_count_of_keywords or text.count(',') < 1:
        last_count_of_keywords = text.count(',')
        selected_keywords = text.split(",")
        selected_keywords_label.config(text=f"Selected: {''.join(selected_keywords)}")


# Create the main window
window = tk.Tk()
window.title("DocPuller")
window.geometry('700x550')
window.resizable(False, False)

# Resize the background image
background_image = Image.open("images/background.jpeg")
resized_image = background_image.resize((800, 600))  # Specify the desired width and height
background_photo = ImageTk.PhotoImage(resized_image)

# Create a label to hold the background image
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Headline
headline = tk.Label(window, text="DocPuller", font=("Arial", 24, "bold"))
headline.pack(pady=10)

# Section 0: Free Text Directory Entry
section0 = tk.Frame(window, width=entrys_width)
section0.pack(pady=10)

directory_label = tk.Label(section0, text="Directories",width=entrys_width)
directory_label.pack()

directory_entry = tk.Text(section0, height=4, width=entrys_width,)
directory_entry.pack()

selected_directory_label = tk.Label(section0, text='Selected:', font=("Arial", 12),width=entrys_width,anchor='w')
selected_directory_label.pack(anchor='w', pady=5)

# Section 1: Date Selection
section1 = tk.Frame(window, width=entrys_width)
section1.pack(pady=10)

from_date_label = tk.Label(section1, text="From:",padx=10)
from_date_label.pack(side="left")

from_date_entry = DateEntry(section1, date_pattern="dd/mm/yy", show_weeknumbers=False)
from_date_entry.pack(side="left")

to_date_label = tk.Label(section1, text="To:",padx=10)
to_date_label.pack(side="left")

to_date_entry = DateEntry(section1, date_pattern="dd/mm/yy", show_weeknumbers=False)
to_date_entry.pack(side="left")

# Section 2: Radio Buttons
section2 = tk.Frame(window, width=entrys_width)
section2.pack(pady=10)

radio_label = tk.Label(section2, text="File Types",width=entrys_width)
radio_label.pack()

radio_var = tk.StringVar()

radio1 = tk.Radiobutton(section2, text="Document Type", variable=radio_var, value="Option 1", )
radio1.pack(side='left', padx=40)

radio2 = tk.Radiobutton(section2, text="Every File Type", variable=radio_var, value="Option 2",)
radio2.pack(side='left')





# Section 3: Free Text Entry
section3 = tk.Frame(window, width=entrys_width)
section3.pack(pady=10)

keyword_label = tk.Label(section3, text="Keywords", width=entrys_width)
keyword_label.pack()

keyword_entry = tk.Text(section3, height=4, width=entrys_width)
keyword_entry.pack()

selected_keywords_label = tk.Label(section3, text='Selected:', font=("Arial", 12), width=entrys_width, anchor='w')
selected_keywords_label.pack(anchor='w',pady=5)

# Section 4: Submit Button
section4 = tk.Frame(window)
section4.pack(pady=10)

submit_button = tk.Button(section4, text="Generate", command=submit, width=20, height=3)
submit_button.pack()

# Bind the directory entry to update the selected directories label
directory_entry.bind("<KeyRelease>", update_selected_directories)
keyword_entry.bind("<KeyRelease>", update_selected_keywords)

# Start the main event loop
window.mainloop()

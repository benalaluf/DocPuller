import subprocess
from tkinter import Tk
from tkinter.filedialog import askdirectory
import sys

# Specify the path to the Python script you want to convert to an executable
script_path = "/real/gui.py"

# Specify additional PyInstaller options if needed
options = [
    "--onefile",  # Generate a single executable file
    "--noconsole"  # Exclude the console window (optional, for GUI applications)
]

# Prompt the user to select the directory for saving the executable
Tk().withdraw()  # Hide the main window
save_dir = askdirectory(title="Select Directory for Saving Executable")

# If the user canceled the directory selection, exit the script
if not save_dir:
    sys.exit()

# Set the output directory option for PyInstaller
output_dir = f"--distpath={save_dir}"
options.append(output_dir)

# Run PyInstaller
command = ["pyinstaller", script_path] + options

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

# Start the progress bar
sys.stdout.write("Conversion progress: [          ]")
sys.stdout.flush()

progress = 0
progress_bar_length = 10
progress_increment = 100 / progress_bar_length

# Read the output and update the progress bar
for line in process.stdout:
    if "Building" in line:
        progress += progress_increment
        num_filled = int(progress / progress_increment)
        num_empty = progress_bar_length - num_filled
        progress_bar = "[" + "=" * num_filled + " " * num_empty + "]"
        sys.stdout.write("\rConversion progress: " + progress_bar)
        sys.stdout.flush()

sys.stdout.write("\nConversion completed!\n")
sys.stdout.flush()

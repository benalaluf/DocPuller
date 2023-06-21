__author__ = 'iBen'

import multiprocessing
import subprocess
from concurrent.futures import ProcessPoolExecutor
import threading
from datetime import datetime
import os
import shutil
import time
from pathlib import Path
from queue import Queue

start_time = 0


class DocPuller:

    def __init__(self):
        self.directorys = ('Downloads', 'Desktop')

        self.months = ('Jun', "Oct", "Dec", 'Mar')
        self.years = ('2023', '2022')

        self.file_types = ('.doc', '.pdf')

        self.key_words = ('test', 'math')

        self.USB_NAME = 'NO_NAME'
        self.login = os.getlogin()
        self.path = rf'C:\Users\{self.login}'
        self.usb_path = self.get_usb_drive_letter()
        print('usbfound',self.usb_path)
        self.folder_name = ''
        self.copy_files = Queue()

    def get_usb_drive_letter(self):
        command = 'wmic logicaldisk where drivetype=2 get caption, volumename'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = result.stdout.replace(' ', '').strip().split('\n')
        for line in result:
            if self.USB_NAME in line:
                return line[0:2] + '\\'
        print('cant find usb')
        exit()

    def is_date(self, time_stamp):
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
        return (file, "is type file " + str(self.is_file_type(file)), "is date " + str(self.is_date(time_stamp)),
                "is special " + str(self.is_key_words(file)))

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
        threads = []
        for file in os.listdir(f'{self.path}\\{dirs}'):
            time_stamp = time.ctime(os.path.getctime(f'{self.path}\\{dirs}\\{file}'))
            if (self.is_date(time_stamp) and self.is_file_type(file)) or self.is_key_words(file):
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(self.get_file_stt(file, time_stamp))
                thread = threading.Thread(target=self.copy_file_to_usb, args=[f'{self.path}\\{dirs}\\{file}'])
                thread.start()
                threads.append(thread)

        for thread in threads:
            thread.join()

    def main_action(self):
        global start_time
        start_time = time.perf_counter()

        pool = multiprocessing.Pool(2)
        for dirs in self.directorys:
            pool.map(self.scan_dir, [dirs])


    def main(self):
        self.set_folder_name()
        self.create_folder_in_usb()
        self.main_action()
        print('done.')
        print(time.perf_counter() - start_time)
        # input()


if __name__ == '__main__':
    DocPuller().main()

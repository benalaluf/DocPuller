__author__ = 'Ben'

import subprocess
import threading
from datetime import datetime
import os
import shutil
import time
from queue import Queue

start_time = 0


class DocPuller:

    def __init__(self, directorys, file_types, key_words, date):
        self.__running = True

        self.__directorys = directorys

        self.__file_types = file_types
        self.__key_words = key_words

        self.date = date

        self.__copy_files = Queue()

        self.__USB_NAME = 'NO_NAME'

        self.__login = os.getlogin()
        self.__path = rf'C:\Users\{self.__login}'
        self.__usb_path = self.__get_usb_drive_letter()

        self.__folder_name = self.__set_folder_name()
        self.__create_folder_in_usb()

    # file specification check
    def __is_date(self, time_stamp):
        is_date = False
        for year in self.date.keys():
            for month in self.date.get(year):
                if time_stamp.split('-')[2] == year and time_stamp.split()[1] == month:
                    is_date = True
        return is_date

    def __is_file_type(self, file):
        return os.path.splitext(file)[1] in self.__file_types

    def __is_key_words(self, file):
        is_key_word = False
        for key_word in self.__key_words:
            if key_word in file:
                is_key_word = True
        return is_key_word

    # locates the usb
    def __get_usb_drive_letter(self):
        command = 'wmic logicaldisk where drivetype=2 get caption, volumename'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = result.stdout.replace(' ', '').strip().split('\n')
        for line in result:
            if self.__USB_NAME in line:
                return line[0:2] + '\\'
        else:
            print('cant find usb')
            exit(1)

    def __get_file_stt(self, file, time_stamp):
        return (file, "is type file " + str(self.__is_file_type(file)), "is date " + str(self.__is_date(time_stamp)),
                "is special " + str(self.__is_key_words(file)))

    def __get_current_date(self):
        return str(datetime.now())[:-10].replace("-", "~").replace(":", ".")

    def __set_folder_name(self):
        self.__folder_name = f'{os.getlogin()} docPull {self.__get_current_date()}'

    def __create_folder_in_usb(self):
        os.chdir(self.__usb_path)
        if not os.path.exists(self.__folder_name):
            os.mkdir(self.__folder_name)

    def __copy_file(self, path, path2):
        try:
            shutil.copy2(path, path2)
        except Exception as e:
            print(e)

    def __copy_file_to_usb(self):
        while self.__running or not self.__copy_files.empty():
            if not self.__copy_files.empty():
                path = self.__copy_files.get()
                thread = threading.Thread(target=self.__copy_file,
                                          args=(path, self.__usb_path + "\\" + self.__folder_name))
                thread.start()

    def __scan_dir(self, dirs):
        path = f'{self.__path}\\{dirs}'
        for file in os.listdir(path):
            time_stamp = datetime.fromtimestamp(os.path.getctime(f'{path}\\{file}')).date().strftime("%d-%m-%Y")
            if (self.__is_date(time_stamp) and self.__is_file_type(file)) or self.__is_key_words(file):
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(self.__get_file_stt(file, time_stamp))
                self.__copy_files.put(f'{path}\\{file}')

    def __scan_dirs(self):
        threads = []
        for dirs in self.__directorys:
            thread = threading.Thread(target=self.__scan_dir, args=(dirs,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        self.__running = False

    def __main_docPuller(self):
        global start_time
        start_time = time.perf_counter()

        scan_thread = threading.Thread(target=self.__scan_dirs)
        copy_thread = threading.Thread(target=self.__copy_file_to_usb)

        scan_thread.start()
        copy_thread.start()

        scan_thread.join()
        copy_thread.join()

    def main(self):
        self.__main_docPuller()
        print('done.')
        print('time:', time.perf_counter() - start_time)


if __name__ == '__main__':
    docPuller = DocPuller(
        ('Desktop', 'Downloads'), ('.pdf', '.doc'), ('test', 'math'), ('Jun', 'May', 'Apr'), ('2023', '2022')
    )

    docPuller.main()

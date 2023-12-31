__author__ = 'Ben'

import subprocess
import threading
import os
import shutil
import time

import constants.config
from docpuller_scripts.docpuller_abs import DocPuller
class DocPullerUSB(DocPuller):

    def __init__(self, directories, file_types, key_words, date):
        super().__init__(directories, file_types, key_words, date)
        self.__USB_NAME = constants.config.USB_NAME

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
            exit(0)

    # creates folder in usb for the files to be copy to
    def __create_folder_in_usb(self):
        os.chdir(self.__usb_path)
        if not os.path.exists(self._folder_name):
            os.mkdir(self._folder_name)

    # copy file from path to path2
    def __copy_file(self, path, path2):
        try:
            shutil.copy2(path, path2)
        except Exception as e:
            print(e)

    # overriding abstract method
    def _pull_files(self):
        while self._running or not self._pull_files_queue.empty():
            if not self._pull_files_queue.empty():
                self._mutex.acquire()
                path = self._pull_files_queue.get()
                self._mutex.release()
                thread = threading.Thread(target=self.__copy_file,
                                          args=(path, self.__usb_path + "\\" + self._folder_name))
                thread.start()

    def main(self):
        starttime = time.perf_counter()
        self.__usb_path = self.__get_usb_drive_letter()
        self.__create_folder_in_usb()
        self._main()

        print(f'finish in: {time.perf_counter() - starttime}')

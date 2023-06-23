__author__ = 'Ben'

import subprocess
import threading
from abc import ABC
from datetime import datetime
import os
import shutil
import time
from queue import Queue

from real.DocPullerScripts.DocPullerGenric import DocPuller

start_time = 0


class DocPullerUSB(DocPuller):

    def __init__(self, directorys, file_types, key_words, date):
        super().__init__(directorys, file_types, key_words, date)
        self.__USB_NAME = 'DOCPULLER'
        self.__usb_path = self.__get_usb_drive_letter()
        self.__create_folder_in_usb()

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

    # creates folder in usb for the files to be copy to
    def __create_folder_in_usb(self):
        os.chdir(self.__usb_path)
        if not os.path.exists(self._folder_name):
            os.mkdir(self._folder_name)

    # copys file from path to path2
    def __copy_file(self, path, path2):
        try:
            shutil.copy2(path, path2)
        except Exception as e:
            print(e)

    # overriding abstract method
    def _pull_files(self):
        while self._running or not self._pull_files_queue.empty():
            if not self._pull_files_queue.empty():
                path = self._pull_files_queue.get()
                thread = threading.Thread(target=self.__copy_file,
                                          args=(path, self.__usb_path + "\\" + self._folder_name))
                thread.start()


if __name__ == '__main__':
    docPuller = DocPullerUSB(
        ('Desktop', 'Downloads'), ('.pdf', '.doc'), ('test', 'math'), {'2023': ('06', '05',)}
    )

    docPuller._main()

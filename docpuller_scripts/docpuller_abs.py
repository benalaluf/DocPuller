__author__ = 'Ben'

import threading
import time
from abc import abstractmethod, ABC
from datetime import datetime
import os
from queue import Queue

from constants.constatns import DOCPULLER_ROOT_DIR


class DocPuller(ABC):
    def __init__(self, directories, file_types, key_words, date):
        self._running = True

        self._directories = directories

        self._file_types = file_types
        self._key_words = key_words

        self._date = (datetime.fromisoformat(date[0]).date(), datetime.fromisoformat(date[1]).date())

        self._pull_files_queue = Queue()
        self._mutex = threading.Lock()

        self._path = DOCPULLER_ROOT_DIR

        self._folder_name = self.__set_folder_name()

    # file specification check

    def __is_date(self, date):
        from_date = self._date[0]
        to_date = self._date[1]
        return from_date <= date <= to_date

    def __is_file_type(self, file):
        return os.path.splitext(file)[1] in self._file_types

    def __is_key_words(self, file):
        is_key_word = False
        for key_word in self._key_words:
            if key_word in file:
                is_key_word = True
        return is_key_word

    def __get_file_stt(self, file, time_stamp):
        return (file, "is type file " + str(self.__is_file_type(file)), "is date " + str(self.__is_date(time_stamp)),
                "is special " + str(self.__is_key_words(file)))

    def __get_current_date(self):
        return str(datetime.now())[:-10].replace("-", "~").replace(":", ".")

    def __set_folder_name(self):
        return f'{os.getlogin()} docPull {self.__get_current_date()}'

    @abstractmethod
    def _pull_files(self):
        pass

    def __scan_dir(self, dir):
        path = os.path.join(self._path, dir)
        for file in os.listdir(path):
            time_stamp = datetime.fromtimestamp(os.path.getatime(os.path.join(path, file))).date()
            if (self.__is_date(time_stamp) and self.__is_file_type(file)) or self.__is_key_words(file):
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print(self.__get_file_stt(file, time_stamp))
                self._mutex.acquire()

                self._pull_files_queue.put(os.path.join(path, file))
                self._mutex.release()

    def _scan_dirs(self):
        threads = []
        for dirs in self._directories:
            thread = threading.Thread(target=self.__scan_dir, args=(dirs,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        self._running = False

    def __main_docpuller(self):
        global start_time
        start_time = time.perf_counter()
        scan_thread = threading.Thread(target=self._scan_dirs)
        pull_thread = threading.Thread(target=self._pull_files)

        scan_thread.start()
        pull_thread.start()

        scan_thread.join()
        pull_thread.join()

    def _main(self):
        self.__main_docpuller()

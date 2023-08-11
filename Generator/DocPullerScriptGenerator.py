from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB


class ScriptGen:

    def __init__(self, is_usb, direcoties, file_type, date, keywords, server_ip, server_port):
        if is_usb:
            self.parms = f'{direcoties}, {file_type}, {keywords}, {date}'

        self.DocPuller_USB_SCRIPT = f"""
        
from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB

def main():

    docPuller = DucPullerUSB({self.parms})

    docPuller.main()
    
    
if __name__ == '__main__':
    main();

        """



    def write_to_file(self):
        with open('docpullerscrip.py', 'w') as f:
            f.write(self.DocPuller_USB_SCRIPT)
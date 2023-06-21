import multiprocessing
import os
import threading

class idk:
    def __init__(self):
        self.path
        self.usb_path = get
    def get_usb_drive_letter():
        command = 'wmic logicaldisk where drivetype=2 get caption volumename'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        result = result.stdout.replace(' ', '').strip().split('\n')
        for line in result:
            if USB_NAME in line:
                return line[0:2] + '\\'


    def is_date(time_stamp):
        # print(time_stamp.split()[4
        # print(time_stamp,time_stamp.split()[4] in year)
        return time_stamp.split()[4] in year and time_stamp.split()[1] in months


    def is_file_type(file):
        return os.path.splitext(file)[1] in file_types


    def is_key_words(file):
        is_key_word = False
        for key_word in key_words:
            if key_word in file:
                is_key_word = True
        return is_key_word


    def get_file_stt(file, time_stamp):
        return (file, "\nis type file " + str(is_file_type(file)), "\nis date " + str(is_date(time_stamp)),
                "\nis special " + str(is_key_words(file)))


    def get_current_date():
        return str(datetime.now())[:-10].replace("-", "~").replace(":", ".")


    def set_folder_name():
        global folder_name
        folder_name = os.getlogin() + 'docPull'


    def create_folder_in_usb(usb):
        os.chdir(usb)
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)


    def copy_file_to_usb(path, usb):
        try:
            shutil.copy2(path, usb + "\\" + folder_name)
        except Exception as e:
            print(e)


    def scan_dir(path,dirs):
        for file in os.listdir(f'{path}\\{dirs}'):
            time_stamp = time.ctime(os.path.getctime(f'{path}\\{dirs}\\{file}'))
            # print(time_stamp)

            if (is_date(time_stamp) and is_file_type(file)) or is_key_words(file):
                print(get_file_stt(file, time_stamp))
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                thread = threading.Thread(target=copy_file_to_usb, args=[f'{path}\\{dirs}\\{file}'])
                thread.start()
                # thread.join()


    def main_action(directorys):
        processs = []
        for dirs in directorys:
            procses = multiprocessing.Process(target=scan_dir, args=(dirs,))
            processs.append(procses)

        for procses in processs:
            procses.join()


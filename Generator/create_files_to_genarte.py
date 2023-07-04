import datetime
import pickle

from DocPullerScripts.DocPullerUsb.DocPullerPreformenc import DocPullerUSB


class create_files_to_generate:

    def __init__(self, is_usb, direcoties, file_type, date, keywords, server_ip=None, server_port=None):
        self.is_usb = is_usb
        self.direcoties = direcoties
        self.file_type = file_type
        self.date = date
        self.keywords = keywords
        self.server_ip = server_ip
        self.server_port = server_port

    def main(self):
        if self.is_usb:
            object = DocPullerUSB(self.direcoties, self.file_type, self.keywords, self.date)

            # Serialize the object instance using pickle
            with open('frozen_object.pkl', 'wb') as file:
                pickle.dump(object, file)

if __name__ == '__main__':
    asdf = create_files_to_generate(True, ('Desktop', ), ('.pdf', '.doc'),
                                    (datetime.date(2020,1,1), datetime.date(2023,1,1)), ('nigger',))
    asdf.main()
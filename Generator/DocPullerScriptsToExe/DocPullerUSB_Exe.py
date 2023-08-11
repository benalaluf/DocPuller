import dill
from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB
class nigga:
    def __init__(self):
        with open(r'DocPullerFrozenObjects/FrozenDocPullerUSB.pkl', 'rb') as file:
            loaded_obj = dill.load(file)

        loaded_obj.main()
if __name__ == '__main__':
  nigga()

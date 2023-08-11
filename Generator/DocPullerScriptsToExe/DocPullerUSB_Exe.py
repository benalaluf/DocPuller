import dill
from DocPullerScripts.DocPullerUsb.usb import DocPullerUSB

if __name__ == '__main__':
    with open(r'DocPullerFrozenObjects/FrozenDocPullerUSB.pkl', 'rb') as file:
        loaded_obj = dill.load(file)

    loaded_obj.main()

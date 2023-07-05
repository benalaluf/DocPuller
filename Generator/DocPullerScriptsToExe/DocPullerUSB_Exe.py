import dill


class DocPullerUSBExe:

    def __init__(self):
        with open('DocPullerObjecets/frozen_DocPullerUSB.pkl', 'rb') as file:
            loaded_obj = dill.load(file)

        loaded_obj.main()


if __name__ == '__main__':
    DocPullerUSBExe()

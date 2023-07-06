import pickle

import dill


class DocPullerUSBExe:

    def __init__(self):
        with open(r'C:\Users\ibena\Documents\GitHub\DocPuller\Generator\DocPullerObjecets\frozen_DocPullerUSB.pkl', 'rb') as file:
            loaded_obj = dill.load(file)

        loaded_obj.main()




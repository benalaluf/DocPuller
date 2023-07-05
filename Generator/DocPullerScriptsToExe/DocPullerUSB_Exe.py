import pickle

import dill

if __name__ == '__main__':

    with open(r'C:\Users\ibena\Documents\GitHub\DocPuller\Generator\DocPullerObjecets\frozen_DocPullerUSB.pkl', 'rb') as file:
        loaded_obj = pickle.load(file)

    loaded_obj.main()

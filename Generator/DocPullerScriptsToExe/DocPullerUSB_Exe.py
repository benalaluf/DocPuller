import pickle

import dill

with open(r'C:\Users\ibena\Documents\GitHub\DocPuller\Generator\DocPullerObjecets\frozen_DocPullerUSB.pkl', 'rb') as file:
    loaded_obj = pickle.load(file)

if __name__ == '__main__':
    loaded_obj.main()

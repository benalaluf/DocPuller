import dill

if __name__ == '__main__':

    with open('DocPullerFrozenObjects/frozen_DocPullerFTPSever.pkl', 'rb') as file:
        loaded_obj = dill.load(file)

    loaded_obj.main()

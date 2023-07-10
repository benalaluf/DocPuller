import dill

if __name__ == '__main__':

    with open('DocPullerObjecets/frozen_DocPullerFTPVictim.pkl', 'rb') as file:
        loaded_obj = dill.load(file)

    loaded_obj.main()

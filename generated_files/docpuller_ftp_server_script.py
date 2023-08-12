

from docpuller_scripts.docpuller_ftp.server_ftp import Server


def main():
    try:
        docPuller = Server("192.168.1.102", 8831, "c:\\")
        docPuller.main()
    except Exception as e:
        print(e)

    


if __name__ == '__main__':
    main()

                    
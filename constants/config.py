import os

# docpuller file types

DOCUMENT_FILE_TYPES = ('.doc', '.docx', '.pdf', '.txt',)
IMAGE_FILE_TYPES = ('.png', '.jpeg', '.jpg')
VIDEO_FILE_TYPES = ('.mp4', '.mov')
AUDIO_FILE_TYPES = ('.mp3', '.wav')

# docpuller_usb
USB_NAME = 'DOCPULLER'

# docpuller_ftp_server
PATH_TO_SAVE = rf'c:\\Users{os.getlogin()}\Desktop'

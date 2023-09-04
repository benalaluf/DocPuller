# DocPuller
## GUI application designed to generate executable DocPuller malware scripts. 
Docpuller script is a script that is designated to obtain desired documents from your “victim’s” device automatically and efficiently by submitting specific or generic parameters.     

![Screen Shot 2023-08-25 at 12 02 12](https://github.com/benalaluf/DocPuller/assets/94129183/c1df8645-f820-4687-bda7-d1973bb45a16)

## How does it work?
the script scans for files that are with the same file type specified and modify data in the range of the dates
or for any file whose name includes one of the keywords, the script will scan for files only in the specified directories.

`(file.type in file_types and from_date <= file.date <= to_date) or file.name in keywords`

** More info coming soon.. **

## Features

Documents can be obtained by using one of the two following methods:

*  Locally – USB flash drive
*  Remotely – client-server

## Getting Started
1. Clone the project to your local machine
   - `git clone https://github.com/benalaluf/DocPuller`
2. Move into the project directly
   - `cd DocPuller`
3. Install the requirements via the requiements.txt file with the following command:
   - `pip install -r requiermetns.txt`
4. run main.py
   - `python main.py`

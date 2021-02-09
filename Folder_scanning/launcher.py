# Python 3.5.4

import folder_scanning
import sys

if len(sys.argv) != 3:
    print("Invalid number of arguments")
    print("launcher.py list_file_path directory_path")
    sys.exit(-5)
    
fs = folder_scanning.folder_scanning_tool()
fs.importList(sys.argv[1])
fs.scan(sys.argv[2])

# returns the compare status.
sys.exit(fs.compare())
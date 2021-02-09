# Python 3.5.4

import os

class folder_scanning_tool():
    def __init__(self):
        # used to read the list file
        self.lines = []
        
        # used to store the detected files
        self.file_list = []
    
    def scan(self, path):
        # gets current directory
        self.file_list = []
        dirname = os.path.dirname(__file__) + r"/"
        test_folder = os.path.join(dirname, path)
        
        file_set = set()

        for dir_, _, files in os.walk(test_folder):
            for file_name in files:
                rel_dir = os.path.relpath(dir_, dirname)
                rel_file = os.path.join(rel_dir, file_name)
                file_set.add(rel_file)
        
        for file in file_set:
            self.file_list.append(file[len(path) + 1 :].replace('\\', '/'))
            
#        print(self.file_list)
        
    def importList(self, listpath):
        # reads a list file
        self.lines = []
        with open(listpath, "r") as listfile:
            for line in listfile.readlines():
                if line.endswith("\n"):
                    # reads the line and gets rid of \n
                    self.lines.append(line[:-1])
                else :
                    self.lines.append(line)
            listfile.close()
#        print(self.lines)
            
    def compare(self):
        differences = list(set(self.lines) - set(self.file_list))
        if len(differences) > 0:
            print("These files are missing")
            print(differences)
            return -1
        
        differences = list(set(self.file_list) - set(self.lines))
        if len(differences) > 0:
            print("These files are not expected")
            print(differences)
            return -2
        
        print("OK")
        return 0
        
if __name__ == '__main__':
    fs = folder_scanning_tool()
    fs.scan(r"test_data\data1")
    fs.importList(r"test_data\list.txt")
    fs.compare()
    
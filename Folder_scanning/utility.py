import os

path = r"test_data\data1"

# gets current directory
file_list = []
dirname = os.path.dirname(__file__) + r"/"
test_folder = os.path.join(dirname, path)

file_set = set()

for dir_, _, files in os.walk(test_folder):
    for file_name in files:
        rel_dir = os.path.relpath(dir_, dirname)
        rel_file = os.path.join(rel_dir, file_name)
        file_set.add(rel_file)

for file in file_set:
    file_list.append(file[len(path) + 1 :].replace('\\', '/'))
    
for item in file_list:
    print(item)
import os

path = r"/Users/user/documents/Udacity-Python/A Secrete Message/prank"

def rename_files():
    file_list = os.listdir(path)
    os.chdir(path)

    for file_name in file_list:
        print(file_name)
        transtable = file_name.maketrans("0123456789", "          ")
        new_name = file_name.translate(transtable)
        os.rename(file_name, new_name)

rename_files()
import os, sys

def rename_files():
    # get files from a folder
    file_list = os.listdir("/home/gnome/Github/PyProgrammingFoundations/prank")
    saved_path = os.getcwd

    os.chdir("/home/gnome/Github/PyProgrammingFoundations/prank")
    saved_path = os.getcwd
    # for each file, rename file
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()

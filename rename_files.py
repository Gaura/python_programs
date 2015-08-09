import os

def rename_files():
    file_list = os.listdir(r"C:\Gaurav\Learn\Programming\Python\prank\prank")
    print(file_list)
    print("Current working directory is " + os.getcwd())
    os.chdir(r"C:\Gaurav\Learn\Programming\Python\prank\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0987654321"))
        print(file_name.translate(None, "0987654321"))

rename_files()

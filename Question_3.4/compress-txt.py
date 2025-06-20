import os
from zipfile import ZipFile

def compress_txt_files():
    
    # define current directory
    current_dir = '.'

    # list all files in current directory 
    files = os.listdir(current_dir)

    # name of zip file
    output_zipfile = "mytxt.zip"

    # all txt files in current directory
    txt_files = [i for i in files if i.endswith('.txt')]

    # compress files into zip file
    with ZipFile(output_zipfile, "w") as zipf:
        for file in txt_files:
            zipf.write(file)
    
    # count number of .txt files and print result message
    count = len(txt_files)
    print(f"There are number of {count} .txt files and compressed into a .zip file")

compress_txt_files()

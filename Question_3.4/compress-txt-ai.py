import os
import zipfile

# This function finds all .txt files in the current directory, compresses them into a ZIP file & prints the count.
def compress_txt_files():
    # Get list of all files in the current working directory
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

    # Count the number of .txt files
    count = len(txt_files)

    # Create a ZIP file and write all .txt files into it
    with zipfile.ZipFile('mytxt.zip', 'w') as zipf:
        for file in txt_files:
            zipf.write(file)

    # Print summary message
    print(f"There are number of {count} .txt files and compressed into a .zip file")

# Execute the function
compress_txt_files()

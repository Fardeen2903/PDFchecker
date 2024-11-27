import hashlib
from tkinter import Tk, filedialog
from difflib import SequenceMatcher

def hash_file(fileName1, fileName2):
    # Use hashlib to store the hash of a file
    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    # Read first file in chunks
    with open(fileName1, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h1.update(chunk)

    # Read second file in chunks
    with open(fileName2, "rb") as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()

def select_files():
    # Set up Tkinter window to select files
    root = Tk()
    root.withdraw()  # Hide the root window

    # Let the user select two files
    file1 = filedialog.askopenfilename(title="Select the first PDF file", filetypes=[("PDF files", "*.pdf")])
    file2 = filedialog.askopenfilename(title="Select the second PDF file", filetypes=[("PDF files", "*.pdf")])

    if file1 and file2:
        return file1, file2
    else:
        print("You must select two files!")
        return None, None

def main():
    file1, file2 = select_files()

    if file1 and file2:
        msg1, msg2 = hash_file(file1, file2)

        if msg1 != msg2:
            print("These files are not identical.")
        else:
            print("These files are identical.")
    else:
        print("File selection was not successful.")

if __name__ == "__main__":
    main()

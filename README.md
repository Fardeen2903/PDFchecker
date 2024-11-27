# PDFchecker
python code for simple program to check two pdf files for identical content

# PDF File Checker

This is a simple Python program that checks if two PDF files are identical by comparing their SHA-1 hashes. The program allows users to upload two PDF files using a graphical interface and determines whether the files are the same or not.

## Features
- Upload two PDF files through a graphical file dialog.
- The program compares the files by calculating their SHA-1 hashes.
- Displays whether the files are identical or not.

## Requirements
- Python 3.x
- `tkinter` (for the graphical file selection dialog, typically comes pre-installed with Python)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/pdfchecker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd pdf-file-checker
    ```

3. Run the script using Python:

    ```bash
    python pdfchecker.py
    ```

4. Select two PDF files when prompted by the graphical file dialog.

## Usage

- When you run the program, a file dialog will prompt you to select the first PDF file.
- After selecting the first file, the dialog will prompt you to select the second PDF file.
- The program will then compare the files by their SHA-1 hash and print the result:
  - If the hashes are identical, it prints: "These files are identical."
  - If the hashes are different, it prints: "These files are not identical."

## License

This project is licensed under the BSD 2-Clause License - see the [LICENSE](LICENSE) file for details.


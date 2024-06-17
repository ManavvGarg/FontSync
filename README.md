# FontSync
Transfer fonts from your old PC to your new one effortlessly. Created by a designer, for designers.

## Building Instructions

If you'd like to customize the program, follow these steps. Otherwise, simply download the executable file from the releases page.

1. Modify the code to suit your requirements.
2. Install PyInstaller from PyPI:
   ```bash
   pip install pyinstaller
   ```
3. Run the following command in your terminal to generate the executable:

   ```bash
   pyinstaller --noconfirm --onefile --windowed --icon "<path-to-your-icon>" --name "FontSync" --clean --add-data "<path-to-your-icon>;." --add-data "<path-to-the-image-used-in-application>;." --paths "<path-of-dir-where-the-python-file-exists>" "<path-of-dir-where-the-python-file-exists>/FontSync.py"
   ```

## Credits

FontSync is a small open-source project. If you decide to distribute it, please credit this repository.

Thank you for supporting open-source software!

# FontSync
 Transfer fonts from your old PC to new with ease

# Build
1. Modify the code acc to your needs or whatever you need
2. install pyinstaller from pypi
3. run below cli command block in terminal

```
pyinstaller --noconfirm --onefile --windowed --icon "<path-to-your-icon>" --name "FontSync" --clean --add-data "<path-to-your-icon>;." --add-data "<path-to-the-image-used-in-application>;." --paths "<path-of-dir-where-the-python-file-exists>"  "<path-of-dir-where-the-python-file-exists>/FontSync.py"
```

# Credits
This is an open source small program. If you do decide to distribute, please give the required credits back to this repo.

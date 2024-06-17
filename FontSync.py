import os
from PIL import Image, ImageTk
import zipfile
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS2",
            os.path.abspath(".")
        ),
        relative
    )

class FontTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FontSync")
        self.root.geometry("300x400")

        # Set custom icon (replace 'icon.ico' with your actual icon file path)
        # set relative path (copy path in windows). Example: C:\\Users\\manav\\OneDrive\\Desktop\\FontSync\\logo.ico
        icon_path = resource_path('<path-to-icon-used-in-tkinter>') #.ico file
        logo_path = resource_path('<path-to-logo-used-in-tkinter>') #.png file

        if os.path.exists(icon_path):
            self.root.iconbitmap(icon_path)
            self.icon = self.load_and_resize_icon(logo_path)

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 14))

        self.frame = ttk.Frame(self.root, padding="20 20 20 20")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create the label with icon and text
        if hasattr(self, 'icon'):
            self.label = ttk.Label(self.frame, text="FontSync", image=self.icon, compound=tk.LEFT, font=('Helvetica', 18))
            self.label2 = ttk.Label(self.frame, text="Font Transfer Made Easy", font=('Helvetica', 10))
        else:
            self.label = ttk.Label(self.frame, text="FontSync", font=('Helvetica', 18))
            self.label2 = ttk.Label(self.frame, text="Font Transfer Made Easy", font=('Helvetica', 10))
        self.label.pack(pady=0)
        self.label2.pack(pady=10)

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=500, mode="determinate")
        self.console = ScrolledText(self.frame, wrap=tk.WORD, height=10, state=tk.DISABLED)

        self.zip_button = ttk.Button(self.frame, text="Zip Fonts", command=self.zip_fonts)
        self.unzip_button = ttk.Button(self.frame, text="Unzip Fonts", command=self.select_zip_file)
        self.about_button = ttk.Button(self.frame, text="About", command=self.about_window)
        self.info_button = ttk.Button(self.frame, text="HowTo / Info", command=self.info_window)

        self.zip_in_progress = False
        self.unzip_in_progress = False

    def load_and_resize_icon(self, logo_path):
        # Open the image file
        image = Image.open(logo_path)
        icon_height = 18

        # Resize the image while maintaining aspect ratio
        width = int(image.width * (icon_height / image.height))
        image = image.resize((width, icon_height), Image.LANCZOS)

        # Convert Image object to PhotoImage object
        return ImageTk.PhotoImage(image)

    def update_console(self, message):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, message + "\n")
        self.console.config(state=tk.DISABLED)
        self.console.see(tk.END)  # Scroll to the end

    def zip_fonts(self):
        if self.zip_in_progress or self.unzip_in_progress:
            messagebox.showinfo("Operation in Progress", "Please wait for the current operation to complete.")
            return

        self.zip_in_progress = True
        self.progress.pack(pady=20)
        self.console.pack(pady=20, fill=tk.BOTH, expand=True)
        self.console.config(state=tk.NORMAL)
        self.console.delete('1.0', tk.END)

        fonts_dir = r'C:\Windows\Fonts'
        zip_filename = 'fonts_backup.zip'
        current_dir = os.getcwd()

        files = [os.path.join(root, file) for root, _, files in os.walk(fonts_dir) for file in files]
        total_files = len(files)

        with zipfile.ZipFile(zip_filename, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
            for i, file_path in enumerate(files):
                zipf.write(file_path, os.path.relpath(file_path, fonts_dir))
                self.progress['value'] = (i + 1) / total_files * 100
                self.root.update_idletasks()
                self.update_console(f"Zipping: {os.path.basename(file_path)}")

        self.progress.pack_forget()
        self.console.pack_forget()
        self.progress['value'] = 0
        self.zip_in_progress = False
        messagebox.showinfo("Success", f"Fonts have been successfully zipped and copied to {current_dir}")

    def unzip_fonts(self, zip_path):
        if self.zip_in_progress or self.unzip_in_progress:
            messagebox.showinfo("Operation in Progress", "Please wait for the current operation to complete.")
            return

        self.unzip_in_progress = True
        self.progress.pack(pady=20)
        self.console.pack(pady=20, fill=tk.BOTH, expand=True)
        self.console.config(state=tk.NORMAL)
        self.console.delete('1.0', tk.END)

        destination_dir = r'C:\Windows\Fonts'

        if not os.path.exists(zip_path):
            messagebox.showerror("Error", f"{zip_path} does not exist.")
            self.progress.pack_forget()
            self.console.pack_forget()
            self.unzip_in_progress = False
            return

        with zipfile.ZipFile(zip_path, 'r') as zipf:
            files = zipf.namelist()
            total_files = len(files)

            for i, file in enumerate(files):
                file_path = os.path.join(destination_dir, file)
                if os.path.exists(file_path):
                    print(f"Skipping existing file: {file_path}")
                    continue
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                zipf.extract(file, destination_dir)
                self.progress['value'] = (i + 1) / total_files * 100
                self.root.update_idletasks()
                self.update_console(f"Unzipping: {file}")

        self.progress.pack_forget()
        self.console.pack_forget()
        self.progress['value'] = 0
        self.unzip_in_progress = False
        messagebox.showinfo("Success", f"Fonts have been successfully unpacked to {destination_dir}")

    def select_zip_file(self):
        zip_path = filedialog.askopenfilename(title="Select Zip File", filetypes=[("Zip Files", "*.zip")])
        if zip_path:
            self.unzip_fonts(zip_path)
    
    def about_window(self):
        messagebox.showinfo("About", f"This was created by a designer for a designer! \nManav Garg (@manavvgarg on GitHub)")
    
    def info_window(self):
        messagebox.showinfo("HowTo/Info", f"This program copies and zips all the fonts you have installed on your system and makes a zip file.\nWhich you can copy to another machine and use this program again to unzip and install all the fonts!\n\n1. You just have to click 'Zip Fonts' button and it will create a zip file in the current directory\n2. Copy the zip file to the new machine and then click 'UnZip Fonts' button and select the zipped file to unzip and install\n\nYes, it's that simple.")

    def start(self):
        self.zip_button.pack(side=tk.TOP, padx=10, ipadx=10, ipady=10)
        self.unzip_button.pack(side=tk.TOP, padx=10, ipadx=10, ipady=10)
        self.about_button.pack(side=tk.TOP, padx=10, ipadx=10, ipady=10)
        self.info_button.pack(side=tk.TOP, padx=10, ipadx=10, ipady=10)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FontTransferApp(root)
    app.start()

import os
import io
import base64
from PIL import Image, ImageTk
import zipfile
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import tempfile

# Get the temporary directory path
temp_dir = tempfile.gettempdir()

        # Base64 encoded icon image
icon_base64 = """
        AAABAAEAIB8AAAEAIAAkEAAAFgAAACgAAAAgAAAAPgAAAAEAIAAAAAAAgA8AACMuAAAjLgAAAAAAAAAAAADMP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD7//8s9///LPf//yz3//8s9///LPf//yz3//8s9///LPf//yz3//8w+///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////PSv//1WD//9Vh///VYf//1WH//9Vh///VYf//1WH//9Vh///UXf//0E///8xB///LPP//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///yz3//+OW///78v//+/D///vw///78P//+/D///vw///78P//+/D///rt///23///7Ln//9t4///NRf//zD3//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////LPP//3oP///78/////////////////////////////////////////////////////////ff//+y4///SVf//zD3//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w+///SVP//9+H///////////////////////////////////////////////////////////////////HL///RU///zD7//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////qr/////7///vx///34f//8cz///PR/////v///////////////////////////////////////+qv///NQv//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD7//9Rd///ikP//45X//+Sb///moP//4Ir///34////////////////////////////////////////+/D//9dn///LPf//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///yzz//+OY///99/////3///33///hj///8Mb///PT///z0v//9dn///76////////////////////////5Jj//8s8///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////LOv//4pH///////////////7//9+F///MQP//zkf//85H///QT///8cr////////////////////////rtP//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///9hs///ikP///vz/////////////8cv//+OV///SVv//zD7//8s7///hjf////7//////////////////+y2///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8s9///ac///9t///+OW///89P///////////////////vr//9p2///LPP//zD3//9Rc///56f//////////////////5Z7//8s9///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MPv//z0z///PQ///++///45f///rr//////////////34///xyf//12j//8s9///MP///zUL//+27//////////////z0///Zbv//yzz//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8s8///cfP///vr////+///lnf//99//////////////9dj//9BO///MPv//zD///8w////LPP//3oL///78////////7bv//85F///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD3//+em/////////////+in///z0f/////////////23///0E7//8w+///MP///zD7//8w9///RVP//9+D///Xa///UXf//zD3//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///7Lj/////////////67b//+7A//////////////vx///WZ///yjr//81B///SVP//zUP//8s9///Xaf//1F3//8w+///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w+///qr//////////////01f//5Zz///78//////////////LP///ik///6rH///jj///uwf//3oL//81D///LPf//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///yzz//+GN//////////////76///lnv//7Ln///78//////////////////////////////z1///pq///34b//9FT///MPv//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MPf//01v///jl//////////////vw///moP//5Jv///HJ///23///9+D///PT///rs///4pH//+uy///88///3oT//8s8///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MPv//45X///77//////////////76///01P//6av//+Wc///km///56T//+6////56P////7////////uvv//zUL//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w+///OR///6az///77//////////////////////////7////+//////////////////////////////rr///UXv//yz3//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w+///ORv//4pH///jk/////v///////////////////////////////////////////////////////+KQ///LPP//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w+///MPv//01n//+GP///tuv//8s////TU///01P//9NT///TU///01P//9NT///TU///01f//34X//8w9///MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MPf//yzz//8xA///ORv//zkj//85I///OSP//zkj//85I///OSP//zkj//85I///MQf//zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MPv//zD7//8w+///MPv//zD7//8w+///MPv//zD7//8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///8w////MP///zD///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
        """


class FontTransferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FontSync")
        self.root.geometry("600x700")
        self.root.iconbitmap(self.load_and_resize_icon(icon_base64, type="icon"))
        self.icon = self.load_and_resize_icon(icon_base64, type="logo")

        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 14))

        self.frame = ttk.Frame(self.root, padding="1 1 1 1")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Create the label with icon and text
        if hasattr(self, 'icon'):
            self.label = ttk.Label(self.frame, text="FontSync", image=self.icon, compound=tk.LEFT, font=('Helvetica', 32))
            self.label2 = ttk.Label(self.frame, text="Font Transfer Made Easy", font=('Helvetica', 18))
        else:
            self.label = ttk.Label(self.frame, text="FontSync", font=('Helvetica', 32))
            self.label2 = ttk.Label(self.frame, text="Font Transfer Made Easy", font=('Helvetica', 18))
        self.label.pack(pady=0)
        self.label2.pack(pady=20)

        self.progress = ttk.Progressbar(self.frame, orient="horizontal", length=500, mode="determinate")
        self.console = ScrolledText(self.frame, wrap=tk.WORD, height=10, state=tk.DISABLED)

        self.zip_button = ttk.Button(self.frame, text="Zip Fonts", command=self.zip_fonts)
        self.unzip_button = ttk.Button(self.frame, text="Unzip Fonts", command=self.select_zip_file)
        self.about_button = ttk.Button(self.frame, text="About", command=self.about_window)
        self.info_button = ttk.Button(self.frame, text="HowTo / Info", command=self.info_window)

        self.zip_in_progress = False
        self.unzip_in_progress = False

    def load_and_resize_icon(self, base64_string, type):
        # Decode Base64 and resize the image
        image_bytes = base64.b64decode(base64_string)
        if type == 'icon':
            with open(f"{temp_dir}\\icon.ico", 'wb') as f:
                f.write(image_bytes)
            return f"{temp_dir}\\icon.ico"
        elif type == 'logo':
            image = Image.open(io.BytesIO(image_bytes))
            icon_height = 32
            width = int(image.width * (icon_height / image.height))
            image = image.resize((width, icon_height), Image.LANCZOS)
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
                    self.progress['value'] = (i + 1) / total_files * 100
                    self.root.update_idletasks()
                    self.update_console(f"Unzipping: {file}")
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
        self.label3 = ttk.Label(self.frame, justify="center", text="Please don't worry if the window says 'Not Responding'.\nWait for few seconds and it will resume.", font=('Helvetica', 10))
        self.label3.pack(pady=7)
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FontTransferApp(root)
    app.start()

import os, shutil
import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import *

window = tk.Tk()
window.title("Disc Backup Tool")
window.rowconfigure(0, minsize=0, weight=1)
window.columnconfigure(1, minsize=0, weight=1)
window.resizable(False, False)

# Labels
lab_backupedDisc = Label(text="Read disc (RX)")
lab_targetDisc = Label(text="Write Disc  (TX)")

# Option menus
optionsDiscs = ["<select disc>", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
str_selectedLoadedDisc = tk.StringVar(window)
str_selectFlushDisc = tk.StringVar(window)

# dropdown menus
opt_readedDisc = OptionMenu(window, str_selectedLoadedDisc, *optionsDiscs)
opt_flushDisc = OptionMenu(window, str_selectFlushDisc, *optionsDiscs)

def main():
    try:
        # change working directory
        os.chdir(str_selectFlushDisc.get() + ':/')

        # copy disc
        src = rf'{str_selectedLoadedDisc.get()}:/'
        dest = rf'{str_selectFlushDisc.get()}:/'
        shutil.copytree(src, dest, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
        showinfo("Backup Tool - Done", "Operation: BACKUPPING\nStatus: DONE")
        return
    except PermissionError:
        showerror("Backup Tool", "Permission error")

btn_copy = Button(text="Backup Disc", command=main)

# grid
lab_backupedDisc.grid(row=0, column=0, padx=5, pady=5)
lab_targetDisc.grid(row=1, column=0, padx=5, pady=5)

opt_readedDisc.grid(row=0, column=1, padx=5, pady=5)
opt_flushDisc.grid(row=1, column=1, padx=5, pady=5)

btn_copy.grid(row=2, column=1, padx=5, pady=5)

# loop
window.mainloop()
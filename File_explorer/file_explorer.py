import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def browseFiles():


    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/", tit  le="Select File",
                                          filetypes=(("all files", "*.*"), ("executables", "*.exe")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.Label(frame, text=app, bg='#263D89')
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


CANVAS = tk.Canvas(root, height=500, width=500, bg='maroon2')
CANVAS.pack()

frame = tk.Frame(root, bg='maroon3')
frame.place(relwidth=0.9, relheight=0.8, relx=0.05, rely=0.05)


Browser = tk.Button(root, text='Browser', padx=10, pady=5, fg='white', bg='magenta2', border="2",command=browseFiles )
Browser.pack()

Run = tk.Button(root, text='Open', padx=9, pady=5, fg='white', bg='magenta3', border="2",command=runApps)
Run.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
    ##Save the file 
with open('save.txt', 'w') as saved:
    for app in apps:
        saved.write(app + ',')

root.mainloop()


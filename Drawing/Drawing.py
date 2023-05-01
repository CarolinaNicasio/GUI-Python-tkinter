import tkinter as tk
from tkinter import filedialog

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing")

        self.canvas = tk.Canvas(master, width=600, height=600)
        self.canvas.pack()

        self.color = "black"
        self.pen_size = 5
        # Pencil Size
        size_btn = tk.Scale(master, from_=1, to=20, orient=tk.HORIZONTAL, command=self.set_pen_size)
        size_btn.pack(side=tk.BOTTOM)

         # Colors
        colors = ["black", "red", "dodgerblue2", "OliveDrab2", "yellow", "orange", "purple", "pink", "white", "magenta2"]
        for i in range(len(colors)):
            colorbtn = tk.Button(master, bg=colors[i], width=2, command=lambda c=colors[i]: self.set_color(c))
            colorbtn.pack(side=tk.LEFT)

        #SAVEBUTTON

        savebutton = tk.Button(master, text="Guardar", command=self.save_drawing, relief=tk.RIDGE, bg="pink", fg="black")

        savebutton.pack(side=tk.TOP)

        #Mouse events to draw with the pen
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw)

    def set_color(self, color):
        self.color = color

    def set_pen_size(self, size):
        self.pen_size = int(size)

    def start_draw(self, event):
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        self.canvas.create_line((self.last_x, self.last_y, event.x, event.y), width=self.pen_size, fill=self.color)
        self.last_x, self.last_y = event.x, event.y
        #SAVE DRAWING
    def save_drawing(self):
        filetypes = (("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*"))
        filename = filedialog.asksaveasfilename(title="Guardar dibujo", filetypes=filetypes, defaultextension=".png")
        if filename:
            if filename.endswith(".png"):
                self.canvas.postscript(file=filename, colormode="color")
                img = tk.PhotoImage(file=filename)
                img.write(filename, format="png")
            elif filename.endswith(".jpg"):
                self.canvas.postscript(file=filename, colormode="color")
                img = tk.PhotoImage(file=filename)
                img.write(filename, format="jpeg")

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()

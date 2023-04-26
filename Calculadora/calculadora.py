from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.configure(bg="#1c1c1e")

        self.display = Entry(master, width=25, font=("Helvetica", 16), justify="right", bd=0)
        self.display.grid(row=0, column=0, columnspan=4, pady=5)
        self.display.configure(bg="white", fg="black")

        # Crear botones para números y operaciones
        button_1 = self.create_button(1, 1, "1", "#d1d1d6")
        button_2 = self.create_button(1, 2, "2", "#d1d1d6")
        button_3 = self.create_button(1, 3, "3", "#d1d1d6")
        button_4 = self.create_button(2, 1, "4", "#d1d1d6")
        button_5 = self.create_button(2, 2, "5", "#d1d1d6")
        button_6 = self.create_button(2, 3, "6", "#d1d1d6")
        button_7 = self.create_button(3, 1, "7", "#d1d1d6")
        button_8 = self.create_button(3, 2, "8", "#d1d1d6")
        button_9 = self.create_button(3, 3, "9", "#d1d1d6")
        button_0 = self.create_button(4, 2, "0", "#d1d1d6")

        button_add = self.create_button(1, 4, "+", "#ff9500")
        button_subtract = self.create_button(2, 4, "-", "#ff9500")
        button_multiply = self.create_button(3, 4, "*", "#ff9500")
        button_divide = self.create_button(4, 4, "/", "#ff9500")

        button_clear = self.create_button(4, 1, "C", "#d1d1d6")
        button_equals = self.create_button(4, 3, "=", "#ff9500")

        # Crear variables para los botones
        self.equation = ""
        self.current = ""
        self.total = 0
        self.new_total = True
        self.decimal = False

    # Función para crear botones
    def create_button(self, row, column, text, bg_color):
        button = Button(self.master, text=text, width=6, height=3, font=("Helvetica", 16), bd=0, bg=bg_color,
                        command=lambda: self.button_click(text))
        button.grid(row=row, column=column, pady=5)
        return button

    # Función para manejar el clic de los botones
    def button_click(self, text):
        if text in "0123456789":
            if self.new_total:
                self.equation = ""
                self.new_total = False
            self.equation += text
            self.current = text
            self.display.delete(0, END)
            self.display.insert(0, self.equation)
        elif text == ".":
            if self.new_total:
                self.equation = "0."
                self.new_total = False
            elif not self.decimal and self.equation != "":
                self.equation += "."
                self.current = "."
                self.display.delete(0, END)
                self.display.insert(0, self.equation)
                self.decimal = True
        elif text in "+-*/":
            if self.current not in "+-*/":
                self.equation += text
                self.current = text
                self.decimal = False
        elif text == "=":
            try:
                self.total = eval(self.equation)
                self.display.delete(0, END)
                self.display.insert(0, self.total)
                self.equation = str(self.total)
                self.new_total = True
            except ZeroDivisionError:
                self.display.delete(0, END)
                self.display.insert(0, "Error")
                self.equation = ""
                self.current = ""
                self.total = 0
                self.new_total = True
                self.decimal = False
        elif text == "C":
            self.display.delete(0, END)
            self.equation = ""
            self.current = ""
            self.total = 0
            self.new_total = True
            self.decimal = False

# Crear ventana principal
root = Tk()
root.configure(bg="white")
root.title("Calculadora")
root.resizable(width=False, height=False)

# Crear instancia de la calculadora
calculator = Calculator(root)

# Ejecutar loop de la ventana
root.mainloop()

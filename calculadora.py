import tkinter as tk
import math

class CalculadoraCientifica:

    def __init__(self, root):
        self.root = root
        self.root.title("☠ Scientific Calculator ☠")
        self.root.geometry("650x750")
        self.root.configure(bg="black")

        self.entrada = tk.Entry(
            root,
            font=("Consolas", 24),
            bg="black",
            fg="red",
            insertbackground="red",
            justify="right"
        )

        self.entrada.pack(fill="x", padx=10, pady=10)

        botones = [
            ["7","8","9","/","sqrt(","("],
            ["4","5","6","*","log("," )"],
            ["1","2","3","-","ln(","^"],
            ["0",".","+","sin(","cos(","tan("],
            ["pi","e","!","C","DEL","="]
        ]

        frame = tk.Frame(root, bg="black")
        frame.pack(expand=True)

        for fila in range(len(botones)):
            for col in range(len(botones[fila])):

                texto = botones[fila][col]

                boton = tk.Button(
                    frame,
                    text=texto,
                    width=8,
                    height=3,
                    bg="black",
                    fg="red",
                    font=("Consolas", 14),
                    relief="solid",
                    bd=2,
                    command=lambda t=texto: self.click(t)
                )

                boton.grid(row=fila, column=col, padx=5, pady=5)

    def click(self, valor):

        if valor == "=":
            self.calcular()

        elif valor == "C":
            self.entrada.delete(0, tk.END)

        elif valor == "DEL":
            texto = self.entrada.get()
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, texto[:-1])

        elif valor == "pi":
            self.entrada.insert(tk.END, "math.pi")

        elif valor == "e":
            self.entrada.insert(tk.END, "math.e")

        elif valor == "sin(":
            self.entrada.insert(tk.END, "math.sin(")

        elif valor == "cos(":
            self.entrada.insert(tk.END, "math.cos(")

        elif valor == "tan(":
            self.entrada.insert(tk.END, "math.tan(")

        elif valor == "sqrt(":
            self.entrada.insert(tk.END, "math.sqrt(")

        elif valor == "log(":
            self.entrada.insert(tk.END, "math.log10(")

        elif valor == "ln(":
            self.entrada.insert(tk.END, "math.log(")

        elif valor == "!":
            try:
                n = int(self.entrada.get())
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, str(math.factorial(n)))
            except:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(0, "ERROR")

        elif valor == "^":
            self.entrada.insert(tk.END, "**")

        else:
            self.entrada.insert(tk.END, valor)

    def calcular(self):
        try:
            expresion = self.entrada.get()
            resultado = eval(expresion)

            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, str(resultado))

        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(0, "ERROR")


root = tk.Tk()
app = CalculadoraCientifica(root)
root.mainloop()

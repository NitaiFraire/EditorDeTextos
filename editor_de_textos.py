from tkinter import *


def nuevo():
    mensaje.set("Nuevo archivo")


def abrir():
    mensaje.set("Abrir archivo")


def guardar():
    mensaje.set("Guardar")


def guardar_como():
    mensaje.set("Guardar como")




root = Tk()
root.title("EditorDeTextosBy:Nitai")

##### Menú superior
#########################
menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

menubar.add_cascade(menu=filemenu, label="Archivo")


##### Caja de texto central
##############################
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=('helvetica', 12))


##### Monitor inferior
##############################
mensaje = StringVar()
mensaje.set("Comienza a editar")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
root.mainloop()

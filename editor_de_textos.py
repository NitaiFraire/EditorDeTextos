from tkinter import *
from tkinter import filedialog as Filedialog
from io import open


ruta = "" # Almacena la ruta de un archivo

def nuevo():

    mensaje.set("Nuevo archivo")
    global ruta
    ruta = ""
    texto.delete(1.0, END)
    root.title("EditorDeTextosBy:Nitai")


def abrir():

    mensaje.set("Abrir archivo")
    global ruta
    ruta = Filedialog.askopenfilename(initialdir=".",
                                      filetypes=(("Archivos de texto", "*.txt"),),
                                      title="Abrir archivo de texto")

    if ruta != "":

        archivo = open(ruta, 'r')
        contenido = archivo.read()
        texto.delete(1.0, END)
        texto.insert('insert', contenido)
        archivo.close()
        root.title(ruta + " - EditorDeTextosBy:Nitai" )


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

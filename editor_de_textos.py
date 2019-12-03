from tkinter import *
from tkinter import filedialog as Filedialog
from io import open


##### FUNCIONES ######## 
#########################

ruta = "" # Almacena la ruta de un archivo

##### Escribir archivo
#########################
def escribir_archivo(ruta):

    contenido = texto.get(1.0, "end-1c") # evitar el salto de linea que se genera al final
    archivo = open(ruta, 'w+')
    archivo.write(contenido)
    archivo.close()
    mensaje.set("Archivo guardado correctamente")


##### Nuevo archivo
#########################
def nuevo():

    mensaje.set("Nuevo archivo")
    global ruta
    ruta = ""
    texto.delete(1.0, END)
    root.title("EditorDeTextosBy:Nitai")


##### Abrir archivo
#########################
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


##### Guardar
########################
def guardar():

    mensaje.set("Guardar")
     
    if ruta != '':
        escribir_archivo(ruta)
    else:
        guardar_como()


##### Guardar como
########################
def guardar_como():

    mensaje.set("Guardar como")
    global ruta
    print(ruta)
    archivo = Filedialog.asksaveasfile(title="Guardar como", defaultextension=".txt")

    if archivo is not None:
        ruta = archivo.name
        escribir_archivo(ruta)
    else:
        mensaje.set("Guardado canceldo")
        ruta = ""




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
menubar.config(bg="#182333", fg="#42a5f5")
filemenu.config(bg="#182333", fg="#42a5f5")


##### Caja de texto central
##############################
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=('helvetica', 12), bg="#1b2738", fg="#a3a5a7")


##### Monitor inferior
############################## selectbackground="red"
mensaje = StringVar()
mensaje.set("Comienza a editar")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")


root.config(menu=menubar)
root.mainloop()
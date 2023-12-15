from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.config(bd = 15)
root.title ("Descargar videos de youtube")

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

def popup():
    messagebox.showinfo("Sobre mi", "Enlace a mi perfil de LinkedIn: No hay")

# Obtener la ruta absoluta del archivo de imagen
ruta_absoluta = os.path.abspath("youtube.png")

imagen_original = Image.open(ruta_absoluta)
imagen_redimensionada = imagen_original.resize((200, 300))
imagen = ImageTk.PhotoImage(imagen_redimensionada)
foto = Label(root, image=imagen, bd=0)
foto.grid(row = 0, column = 0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff = 0)

menubar.add_cascade(label="Mas informacion", menu=helpmenu)
helpmenu.add_command(label="Informacion del desarrollador",command = popup)
menubar.add_command (label="Salir", command=root.destroy)

instrucciones = Label(root, text="Ingrese un link de Youtube para descargar\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)

root.mainloop()
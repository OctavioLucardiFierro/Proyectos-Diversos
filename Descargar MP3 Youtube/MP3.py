import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
import threading

class DescargadorAudioYouTube:
    def __init__(self, master):
        self.master = master
        self.master.title("Descargador de Audio de YouTube")
        self.master.geometry("400x150")
        self.master.configure(bg='#2E2E2E')  # Fondo oscuro

        self.label_instrucciones = ttk.Label(
            master, text="Ingrese el enlace de YouTube:", foreground="white", background='#2E2E2E')
        self.label_instrucciones.grid(row=0, column=0, padx=10, pady=10)

        self.entry_enlace = ttk.Entry(master, width=40)
        self.entry_enlace.grid(row=1, column=0, padx=10, pady=5)

        self.boton_descargar = ttk.Button(
            master, text="Descargar", command=self.descargar_audio, style='TButton')
        self.boton_descargar.grid(row=2, column=0, pady=10)

    def descargar_audio(self):
        enlace_youtube = self.entry_enlace.get()

        if enlace_youtube:
            # Iniciar un hilo para descargar el audio y evitar bloquear la interfaz gráfica
            threading.Thread(target=self.descargar_audio_thread, args=(enlace_youtube,)).start()
        else:
            self.mostrar_mensaje("Por favor, ingrese un enlace de YouTube válido.")

    def descargar_audio_thread(self, enlace_youtube):
        try:
            video = YouTube(enlace_youtube)
            stream = video.streams.filter(only_audio=True).first()
            stream.download(output_path=".", filename_prefix="OLF")

            self.mostrar_mensaje("Descarga completada.")
        except Exception as e:
            self.mostrar_mensaje(f"Error: {str(e)}")

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Mensaje", mensaje)


def iniciar_aplicacion():
    root = tk.Tk()
    root.style = ttk.Style()
    root.style.configure(
        'TButton',
        background='#4CAF50',  # Color verde para el botón
        foreground='white',  # Texto en color blanco
    )
    app = DescargadorAudioYouTube(root)
    root.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()

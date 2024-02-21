from pytube import YouTube

def descargar_video():
    url = input("Por favor, introduce la URL del video de YouTube: ")
    youtube = YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()

descargar_video()

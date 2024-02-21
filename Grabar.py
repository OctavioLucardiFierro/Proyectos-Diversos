import tkinter as tk
import threading
import cv2
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
from PIL import ImageGrab

class ScreenRecorder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screen and Audio Recorder")

        self.start_button = tk.Button(self.root, text="Iniciar Grabación", command=self.start_recording)
        self.stop_button = tk.Button(self.root, text="Detener Grabación", command=self.stop_recording, state=tk.DISABLED)

        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)

        self.recording = False
        self.recording_thread = None
        self.audio_stream = None
        self.audio_frames = []
        self.video_writer = None

    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.audio_frames = []
        self.audio_stream = sd.InputStream(callback=self.audio_callback)
        self.audio_stream.start()

        self.recording_thread = threading.Thread(target=self.record_screen_and_audio)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        self.audio_stream.stop()
        self.audio_stream.close()

    def audio_callback(self, indata, frames, time, status):
        if self.recording:
            self.audio_frames.append(indata.copy())

    def record_screen_and_audio(self):
        width, height = ImageGrab.grab().size
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.video_writer = cv2.VideoWriter("screen_recording.mp4", fourcc, 20.0, (width, height))

        while self.recording:
            screenshot = ImageGrab.grab()
            frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            # Guardar el frame en el video
            self.video_writer.write(frame)

        self.video_writer.release()

        # Guardar el audio en un archivo WAV
        audio_data = np.vstack(self.audio_frames)
        write("audio_recording.wav", 44100, audio_data)

if __name__ == "__main__":
    app = ScreenRecorder()
    app.root.mainloop()

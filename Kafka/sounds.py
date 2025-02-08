from playsound import playsound
import os
import threading
import time
def background_sound():
    playsound(sound='background.mp3',block=False)
def scream_sound():
    playsound(sound='scream.mp3',block=False)
def whisper_sound():
    def loop():
        while True:
            playsound(sound='whispers.mp3',block=False)
            time.sleep(5)
    sound_thread=threading.Thread(target=loop)
    sound_thread.daemon=True
    sound_thread.start()
def door_sound():
    playsound(sound='door.mp3',block=False)
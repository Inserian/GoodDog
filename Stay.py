import RPi.GPIO as GPIO
from gtts import gTTS
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

while True:
    if GPIO.input(18):
        tts = gTTS("Stay", lang='en')
        tts.save("stay.mp3")
        os.system("mpg321 stay.mp3")

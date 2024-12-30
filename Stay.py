import RPi.GPIO as GPIO
from gtts import gTTS
import os
import time

# Constants
BUTTON_PIN = 18
AUDIO_FILE = "stay.mp3"

# Function to play audio
def play_audio(file_path):
    os.system(f"mpg321 {file_path}")

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Use pull-up resistor for button

# Pre-generate TTS audio file to avoid redundant generation
if not os.path.exists(AUDIO_FILE):
    tts = gTTS("Stay", lang='en')
    tts.save(AUDIO_FILE)

try:
    print("Waiting for button press...")
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Button pressed (active-low)
            print("Button pressed, playing audio...")
            play_audio(AUDIO_FILE)
            time.sleep(0.3)  # Debounce delay to prevent rapid triggering
except KeyboardInterrupt:
    print("\nExiting program...")
finally:
    GPIO.cleanup()  # Clean up GPIO settings

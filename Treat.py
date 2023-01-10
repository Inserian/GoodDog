import speech_recognition as sr
import serial

ser = serial.Serial('COM3', 9600)

# Set up the recognizer
r = sr.Recognizer()

def treat():
    print("Dispensing treat...")
    ser.write(b'1')

while True:
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        command = r.recognize_google(audio)
        print("You said: " + command)

        if command.lower() == "treat":
            treat()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

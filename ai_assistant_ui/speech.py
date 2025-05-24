import speech_recognition as sr
import threading
from command import parse_command

transcribed_text = "Listening..."
display_text = transcribed_text
display_color = (0, 255, 0)  # Green

def update_display_with_command(cmd):
    global display_text, display_color, transcribed_text
    display_text = f"Command: {cmd}"
    display_color = (0, 255, 255)  # Yellow

    def reset_display():
        global display_text, display_color
        display_text = transcribed_text
        display_color = (0, 255, 0)

    threading.Timer(2.0, reset_display).start()

def listen_in_background():
    global transcribed_text, display_text, display_color
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        with mic as source:
            try:
                audio = recognizer.listen(source, timeout=5)
                spoken = recognizer.recognize_google(audio)
                transcribed_text = f'You said: "{spoken}"'

                cmd = parse_command(spoken)
                if cmd:
                    update_display_with_command(cmd)
                else:
                    display_text = transcribed_text
                    display_color = (0, 255, 0)

            except sr.WaitTimeoutError:
                transcribed_text = "Listening..."
                display_text = transcribed_text
                display_color = (0, 255, 0)
            except sr.UnknownValueError:
                transcribed_text = "Could not understand"
                display_text = transcribed_text
                display_color = (0, 0, 255)
            except sr.RequestError:
                transcribed_text = "API error"
                display_text = transcribed_text
                display_color = (0, 0, 255)

def start_listening():
    threading.Thread(target=listen_in_background, daemon=True).start()

import speech_recognition as sr
import threading

transcribed_text="Listening..."

def listen_in_background():
    global transcribed_text
    recognizer=sr.Recognizer()
    mic=sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
    while True:
            with mic as source:
                try:
                    audio = recognizer.listen(source, timeout=5)
                    spoken = recognizer.recognize_google(audio)
                    transcribed_text = f'You said: "{spoken}"'
                except sr.WaitTimeoutError:
                    transcribed_text = "Listening..."
                except sr.UnknownValueError:
                    transcribed_text = "Could not understand"
                except sr.RequestError:
                    transcribed_text = "API error"

def start_listening():
    threading.Thread(target=listen_in_background, daemon=True).start()

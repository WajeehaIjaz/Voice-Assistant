import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(f"You said: {data}")  # Better feedback
            return data
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            print("Could not request results; check your internet connection")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == "__main__":
    
    print("Say 'Hello' to activate me...")
    wake_word = sptext()
    
    # Fixed: removed extra space after "hello"
    if wake_word and "hello" in wake_word.lower():
        speechtx("Hello, I am Joe. How can I help you?")
        
        while True:
            data1 = sptext()
            
            if not data1:
                continue
                
            data1 = data1.lower()

            if "your name" in data1:
                speechtx("My name is Joe")

            elif "old are you" in data1:
                speechtx("I am 7 years old")

            elif "time" in data1:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speechtx(f"The time is {current_time}")

            elif "youtube" in data1:
                speechtx("Opening YouTube")
                webbrowser.open("https://www.youtube.com/")

            elif "google" in data1:
                speechtx("Opening Google")
                webbrowser.open("https://www.google.com/")

            elif "joke" in data1:
                speechtx("Here's a joke for you")
                joke1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke1)
                speechtx(joke1)

            elif "play song" in data1 or "song" in data1:
                # Fixed: use EITHER r"" OR \\ not both
                add = r"c:\Users\Affan laptop\Music"
                try:
                    listsong = os.listdir(add)
                    print(f"Songs found: {listsong}")
                    
                    song_found = False
                    for song in listsong:
                        if song.endswith('.mp3'):
                            speechtx(f"Playing {song}")
                            os.startfile(os.path.join(add, song))
                            song_found = True
                            break
                    
                    if not song_found:
                        speechtx("No MP3 files found in Downloads folder")
                except Exception as e:
                    print(f"Error: {e}")
                    speechtx("Sorry, I couldn't access your music folder")

            elif "exit" in data1 or "bye" in data1:
                speechtx("Thank You. Goodbye!")
                break
            
            else:
                speechtx("Sorry, I didn't understand that command")
    else:
        print("'Hello' not detected. Please try again.")
        speechtx("I didn't hear the wake word. Please say Hello to start.")
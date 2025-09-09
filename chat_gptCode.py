import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    # Check the command and perform the respective actions
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        webbrowser.open_new_tab("https://youtube.com")
    elif "open facebook" in command.lower():
        webbrowser.open("https://facebook.com")
    elif "play lemonade on youtube" in command.lower():
        webbrowser.open("https://youtu.be/ZVgergj8Xe4?si=DEhDNLHUhqR8La-g")
    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print(f"Recognized word: {word}")

            if word.lower() == "wake up":
                speak("Jarvis is awake!")
                print("Jarvis is now active. Please give a command.")
                
                # Now listen for the next command
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")
                
                processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
        except Exception as e:
            print(f"Error: {e}")

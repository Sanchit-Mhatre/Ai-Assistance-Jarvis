import speech_recognition as sr
import webbrowser
import pyttsx3
import urllib.parse

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Saying: {text}")  # Debug: Print what the bot is saying
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    print(f"Processing command: {command}")  # Debug: Print the command being processed
    
    # Normalize the command to lowercase to make comparisons easier
    command = command.lower()

    if "open google" in command:
        print("Opening Google")  # Debug: Command recognized
        webbrowser.open("https://google.com")
    elif "open youtube" in command:
        print("Opening YouTube")  # Debug: Command recognized
        webbrowser.open_new_tab("https://youtube.com")
    elif "open facebook" in command:
        print("Opening Facebook")  # Debug: Command recognized
        webbrowser.open("https://facebook.com")
    elif "play" in command and "on youtube" in command:
        # Extract the song name after 'play' and 'on youtube'
        song_name = command.replace("play", "").replace("on youtube", "").strip()
        
        print(f"Extracted song name: '{song_name}'")  # Debug: Show extracted song name
        
        if song_name:  # Ensure that there's a song name extracted
            encoded_song_name = urllib.parse.quote(song_name)
            print(f"Encoded song name: '{encoded_song_name}'")  # Debug: Show encoded song name
            
            # Construct the search URL
            search_url = f"https://www.youtube.com/results?search_query={encoded_song_name}"
            print(f"Opening URL: {search_url}")  # Debug: Show the final URL being opened
            webbrowser.open(search_url)
            speak(f"Playing {song_name} on YouTube.")

    else:
        speak("Sorry, I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")  # Debug: Indicate it's listening
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print(f"Recognized word: {word}")  # Debug: Print the recognized word

            if word.lower() == "wake up":
                speak("Jarvis is awake!")
                print("Jarvis is now active. Please give a command.")
                
                # Now listen for the next command
                with sr.Microphone() as source:
                    print("Listening for command...")  # Debug: Indicate it's listening for command
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                command = recognizer.recognize_google(audio)
                print(f"Command received: {command}")  # Debug: Show the command recognized
                
                processCommand(command)

        # except sr.UnknownValueError:
        #     print("Sorry, i cann't understand the audio.")  # Debug: Print error when unable to understand
        # except sr.RequestError as e:
        #     print(f"Speech recognition service error: {e}")  # Debug: Print service error
        except Exception as e:
            print(f"Error: {e}")  # Debug: Print any other errors

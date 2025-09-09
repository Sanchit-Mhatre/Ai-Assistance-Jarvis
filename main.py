import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests


#pip install pocketsphinx 

recongnizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "d093053d72bc40248998159804e0e67d"


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in  c.lower():
        webbrowser.open_new_tab("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlinnes?country=inus&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()
            
            #extract the articles
            articles = data.get('articles',[])
            
            # print the headline
            for article in articles:
                speak(article['title'])
    else:
        #Lets OpenAI handles the request
        pass
        
        
    
if __name__ == "__main__":
    speak(" Initialiszing Jarvis... ")
while True:    
    # listen for wake word
    
    # obtain from the microphone
    r = sr.Recognizer()
    
    
    
    print("recongnozing...")        
    # recognize speech using Sphinx
    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source , timeout=2, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "wake up"):
            speak("Ya")
            #listen for command
            with sr.Microphone() as source:
                print("Jarvis Active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print(command) # additional
                
                processCommand(command)
                
    except Exception as e:
        print("Error; {0}".format (e))
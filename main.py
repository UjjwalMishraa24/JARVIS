import speech_recognition as sr
import webbrowser
import pyttsx3
import music_lib
import requests

r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "50c13adf-2c26-419b-8365-ed4009e33be5"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    c = c.lower()

    if "open chat" in c:
        webbrowser.open("https://chatgpt.com/")
    elif "open google" in c:
        webbrowser.open("https://google.com/")
    elif "chess" in c:
        webbrowser.open("https://chess.com/")
    elif "open insta" in c:
        webbrowser.open("https://instagram.com/")
    elif "corporate labour chowk" in c:
        webbrowser.open("https://linkedin.com/")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com/")
    elif c.startswith("play"):
        parts = c.split(maxsplit=1)
        if len(parts) > 1:
            song = parts[1]
            link = music_lib.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak(f"Sorry, I couldn't find the song {song}.")
        else:
            speak("Please specify a song name.")
    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])[:5]  # Limit to top 5
            for article in articles:
                speak(article["title"])
        else:
            speak("Sorry, I could not fetch the news at the moment.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Listening for 'Jarvis'...")
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
                word = r.recognize_google(audio)
                if word.lower() == "jarvis":
                    speak("Yes?")
                    with sr.Microphone() as source:
                        audio = r.listen(source, timeout=5)
                        command = r.recognize_google(audio)
                        process_command(command)
        except sr.WaitTimeoutError:
            continue  # Don't print anything, just wait again
        except sr.UnknownValueError:
            print("Didn't catch that.")
        except Exception as e:
            print(f"Jarvis error: {e}")

            
            

    
            


    
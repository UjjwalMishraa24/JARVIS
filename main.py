import speech_recognition as sr
import webbrowser
import pyttsx3
import music_lib
import requests

r = sr.Recognizer()
engine = pyttsx3.init()
newsapi ="50c13adf-2c26-419b-8365-ed4009e33be5"

def speak (text):
    engine.say(text)
    engine.runAndWait()


def process_command(c):
   
   
   if "open chat" in c.lower():
      webbrowser.open("https://chatgpt.com/")
   elif "open google" in c.lower():
      webbrowser.open("https://google.com/")  
   elif "chess" in c.lower():
      webbrowser.open("https://chess.com/")  
   elif "open insta" in c.lower():
      webbrowser.open("https://instagram.com/")  
   elif "corporate labour chowk" in c.lower():
      webbrowser.open("https://linkedin.com/")  
   elif "open youtube" in c.lower():
      webbrowser.open("https://Youtube.com/")  
   elif  c.lower().startswith ("Play") :
      song = c.lower().split(" ")[1]
      link = music_lib.music[song]
      webbrowser.open(link)  
   elif "news" in c.lower():
      r= requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
      if r.status_code == 200:
         data = r.json()
         articles = data.get("articles",[])
         for article in articles:
            speak(article["title"])
         


if __name__ == "__main__":
    speak("Initializing Jarvis..................")
    # listen for the wake word "Jarvis"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using Jarvis
        print("recognising")
        try:
          with sr.Microphone() as source:
            print("Listening.....")   
            audio = r.listen(source , timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
          
          if (word.lower() == "Jarvis"):
                speak("ya")
                with sr.Microphone() as source:
                  print("Jarvis activated....")   
                  audio = r.listen(source)
                  command = r.recognize_google(audio)
                  process_command(command)


        except Exception as e:
          print("Jarvis error; {0}".format(e))
            
            

    
            


    
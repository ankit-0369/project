import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening Sir!")  

    speak("how can i help you sir?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print ("Recognizing...")    
        query = r.recognize_google(audio , language = 'en-in')
        print (f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nvsankit2020@gmail.com', 'ueeqvvntmfspnsnd')
    server.sendmail('nvsankit2020@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            speak("opening google")
            webbrowser.get(chrome_path).open("https://google.com")

        elif 'open stack overflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")   

        elif 'jarvis' in query:
            speak ("i am listening sir!")


        elif 'play music' in query:
                song1 = "c:\\ankit\\harrypotter.mp3"
                speak("playing harry potter theme music")
                os.startfile(song1)
        # elif 'play breathless song' in query:
        #     music_dir = 'C:\\ankit\\breatheless.mp3'
        #     songs2 = os.listdir(music_dir)
        #     print(songs2)    
        #     os.startfile(os.path.join(music_dir, songs2[0]))
        elif 'pause' in query:
            speak("to pause the song you can click on pause button in upper of num lock button on keyboard")


        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening visual studio code ")
        
        elif 'change your voice' in query:
            engine.setProperty('voice', voices[1].id)
            speak("voice has been changed")

        elif 'exit' in query:
            speak("thanks for using me sir! you can call me anytime i will be present")
            exit()
        
        elif 'close' in query:
            speak("thanks for using me sir! you can call me anytime i will be present")
            exit()
        
        


        # elif 'open whatsapp' in query:
        #     whatPath = "C:\\Users\\lenovo\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        #     os.startfile(whatPath)

        elif 'open chrome' in query:
            chromePath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            speak("opening chrome")
            os.startfile(chromePath)

        elif 'open youtube' in query:
           webbrowser.get(chrome_path).open("https://youtube.com")
        
        elif 'twinkle twinkle little star' in query:
            speak("Twinkle twinkle little star;How I wonder what you are;Up above the world  so high;Like a diamond in the sky;")
            speak("any thing else i can help!")
            speak("listening")
        elif 'send email to ankush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ankushkumargaya985260@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ANKUSH. I am not able to send this email")    
          
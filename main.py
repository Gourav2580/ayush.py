import pyttsx3 # text to speak conversion
import speech_recognition as sr # listning program voice
import datetime # date and time for wishme function
import wikipedia #modul
import webbrowser
import os


engine = pyttsx3.init('sapi5') # this ia api to take inbild window voice F/M
voice = engine.getProperty('voices') # like google search engine
print(voice[1].id) #vioce mail or femail
engine.setProperty('voice', voice[1].id)


def speak(audio): # work argument sapeak only audio pronounce (speak function)
    engine.say(audio) # audio string said
    engine.runAndWait() # this is function

     
def wishMe(): # function wish
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morling!")
        

        elif hour>=12 and hour<18:
             speak(" good afternoon!")

        else:
            speak("good evening!")

        speak(" i am python assistance sir what can i do for you")        
def takeCommand(): # microphone input take for laptop

    r = sr.Recognizer() # this is ciass oudio reconization
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1  # audio listan python assistant and hold one minute                                                                                                                                      
        r.energy_threshold = 2000 # peaker listning power increase
        r.phrase_threshold = 2
        audio = r.listen(source) 

    try:    # any error come in program
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e: # any case program not listning
       # print(e)
       print("say that again please...")
       return "None" # this is string and any problum come then none is return
    return query   

if __name__ == "__main__": # here main methode start
   wishMe()
   while True:
       query = takeCommand().lower() # takecommand audio takean by microphone and convert in string
       

       if 'wikipedia' in query:       
           speak('searching wikipedia...')
           query = query.replace("wikipedia", "") #"" blank to replace wikipedia for result
           result = wikipedia.summary(query, sentences=2)
           speak("according to wikipedia")
           speak(result)    

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")

       elif 'open google' in query:
            webbrowser.open("google.com")

       elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow")

       elif 'play music' in query:  
           music_dir = 'D:\\ Non critical\\songs\\Favorite songs2'
           song = os.listdir(music_dir)
           print(song)
           os.startfile(os.path.join(music_dir, song[0]))

       elif 'what is time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"sir the time is {strTime}")

       elif 'introduce yourself' in query:
           speak("my name is python assistant and i devlop by ayush kumar")

       elif 'vc of ptu' in query or 'vc of ikgptu' in query or 'vice chanclar of ikgptu' in query:
           speak("vc of ikgptu is ajay kumar shama")    
           
       elif 'how are you' in query:
           speak("i am fine thank you what can i do for you")  

       elif 'hod of ece' in query or 'satvir singh' in query or 'doctor satvir singh' in query:
           speak(" hade of department of ece department is doctor satvir singh")
           speak("satvir singh office in cb1 and room number 308")

       elif 'Avtar singh buttar' in query or 'dctor avtar singh buttar' in query:           
           speak("avtar singh butter is assistant professor of ece department")
           speak("avtar singh butter office 3rd flour of cb1 and room number 307")

       elif 'chandan preet kaur' in query or 'chandan mam' in query or 'chandan maidam' in query:
           speak("chandanpreet kaur is assistant professor of ece department")
           speak("chandanpreet kaur office is 3rd flour of cb1 and romm number 311")
                
       elif 'jyotsna yadav' in query:
           speak("jyotsna yadav is assistant professor of ece department")

       elif 'rakesh kumar' in query:
           speak("rakesh kumar sir is assistant professor of ece department and office is cb1 and room 211")  

       elif 'rakesh goyal' in query:
           speak("rakesh goyal sir is assistant professor of ece department and office 2rd flour cb1 room 207")

       elif 'dalveer kaur' in query:
           speak("dalveer kaur is assistant professor of ece department and office is 3rd flour of cb1 room 306")

       elif 'amit gupta' in query:
           speak(" amit gupta sir is assistant professor of ece department office is 2nd flour of cb1 and room 206")
          
       elif 'sandeep verma' in query or 'sandeep sir' in query:
          speak("sandeep varma is assistant professor of ece department")
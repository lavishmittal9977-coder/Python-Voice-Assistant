import speech_recognition as sr
import webbrowser
from urllib.parse import quote
import subprocess
from speaker import speak 
from datetime import datetime
from volume_control import volume_up,volume_down,mute,unmute
from wiki_search import search_wikipedia
from command_processor import process_command
recognizer=sr.Recognizer()
while True:
    try:
        with sr.Microphone() as source:

            print("Speak Something....")
            
            audio=recognizer.listen(source)
        print("Recognizing....")
            
        text=recognizer.recognize_google(audio)
        print("You said:",text)
        command=process_command(text)
        print("command:",command)
        if command=="exit":
            speak("Good bye")
            print("Good bye!")
            break
        elif command=="greeting":
            speak("Hello!How can I help you?")
        elif command=="morning":
            speak("Good morning! How can I help you?")
        elif command=="afternoon":
            speak("Good Afternoon! How can I help you?")
        elif command=="evening":
            speak("Good evening! How can I help you?")
        elif command=="time":
            now=datetime.now()
            current_time=now.strftime("%I:%M %p")
            speak("The Current time is"+current_time)   
            print("Current time:",current_time)
        elif command=="date":
            now=datetime.now()
            current_date=now.strftime("%d %B %Y")
            speak("Today's Date is"+current_date)
            print("Today's Date :",current_date)
        elif command=="vs_code":
            speak("Opening Visual Studio code")
            subprocess.Popen("code",shell=True)
        elif command=="chrome":
            speak("Opening Chrome")
            subprocess.Popen("start chrome",shell=True)
        elif command=="volume_up":
            speak("Increasing Volume")
            volume_up()
        elif command=="volume_down":
            speak("Decreasing Volume")
            volume_down()
        
        elif command=="unmute":
            speak("Unmuting Volume")
            unmute()
        elif command=="mute":
            speak("Muting volume")
            mute()
        elif command=="wikipedia":
            if "who is" in text.lower():
               query=text.lower().replace("who is","",1)
            elif "what is" in text.lower():
                query=text.lower().replace("what is","",1)
            speak("Searching Wikipedia")
            answer=search_wikipedia(query)
            print("Answer:",answer)
            speak(answer)
        elif command=="explorer":
            speak("Opening File Explorer")
            subprocess.Popen("explorer.exe")
        elif command=="youtube_search":
            query=text.lower().replace("youtube search","",1)
            query=quote(query)
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
        elif command=="google_search":
            speak("searching on google")
            query=text.lower().replace("search ","",1)
            query=quote(query)
            webbrowser.open("https://www.google.com/search?q="+query)
       
        elif command=="play_music":
            if "play music" in text.lower():
               song=text.lower().replace("play music","",1)
            else:
                song=text.lower().replace("play","",1)
            speak("Playing "+song)
            song=quote(song)
            webbrowser.open("https://www.youtube.com/results?search_query="+song)
        elif command=="youtube":
            speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com/")
        
        elif command=="google":
            speak("Opening Google")
            webbrowser.open("https://www.google.com/")
        elif command=="gmail":
            speak("Opening gmail")
            webbrowser.open("https://mail.google.com")
        elif command=="notepad":
            speak("Opening notepad")
            subprocess.Popen("notepad.exe")
        elif command=="calculator":
            speak("Opening calculator")
            subprocess.Popen("calc.exe")
        else:
            speak("Sorry, I don't know that command.")
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        speak("Sorry, I could not understand")
    except sr.RequestError:
        print("Check Your Internet Connection")
        speak("Check Your Internet Connection")
            
        
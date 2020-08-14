import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib


dict={'nikunj':'nikunjnasit90996@gmail.com','nik':'niknasit90996@gmail.com',
      'niks':'170303108051@paruluniversity.ac.in'}
#pyttsx3 aa ake avu module 6 j bolva mate work kre 6
n=9099651249
engine=pyttsx3.init('sapi5')
#sapi5 is microsoft api for more info there go
voices=engine.getProperty('voices')
#print(voices[1].id)
#jo voices[0] aa mara pc ma boy nu 6 and jo girl nu joi aa to ake lakhvu
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning!")

    elif(hour>=12 and hour<18):
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("hello, i am robot of nikunj,please tell me how may i help you")

#takecommand are take to the stringand return to the microphone using return str 
def takeCommand():
    #it takes microphone input from the user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #seconds of non-speaking audio before we consider the speaking audio(gef pde)
        #jo r.energy_threshold=300 to the minimum audio energy are consider
        r.pause_threshold =1
        #source are delecred to how to use and how many of source 
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception:
        #print(e)

        print("said that again please...")
        #that none are not a python none that are the string form the none
        return "None"
    return query
#the SMTPare to the bulit in module in python there use to mail sending to the particular mail
def sendEmail(to,content):
    #there are port number are fix to  sending mail
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    with open("binary2","bw") as  bin_file:
        bin_file.write(n.to_bytes(10,'little'))

    with open("binary2","br") as bin_file:
        return(int.from_bytes(bin_file.read(10),'little'))

    server.login('niknasit90996@gmail.com',print(bin_file.read()))
    server.sendmail('niknasit90996',to,content)
    server.close()
if __name__ == "__main__":
    wishme()
    #if output are continue to the running loop are using  while loop
    while True:
    #if 1:
        #there are all query source are lower charater ...then query are maTHC
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("serching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("Acording to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("openinng youtube ")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("opening google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("opening stackoverflow")

        elif 'play music' in query:
            music_dir='E:\\song'
            songs = os.listdir(music_dir)
            s=(random.choice(songs))
            os.startfile(os.path.join(music_dir,s))
        
        elif 'play video' in query:
            video_dir=webbrowser.open("youtube.com")
            v=(random.choice(video_dir))
            os.startfile(os.path.join(video_dir,v))    
        
        elif 'the time' in query:
            strTime = datetime.datetime.now()
            speak(f" hello nikunj sir, the time  is {strTime}")
            print(f"sir, the time  is {strTime}")

        elif 'open visual studio code' in query:
            codepath = "C:\\Users\\Paras\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("open are visual stdio")

        elif 'open facebook account nikunj' in query:
            webbrowser.open("https://www.facebook.com/nikunj.nasit.90")
            speak("opening  facebook")

        elif 'open yahoo' in query:
            webbrowser.open("https//www.yahoo.com")
            speak("opening yahoo")
        
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
            speak("opeing whatsapp")

        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opeining flipkart")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open browser' in query:
            webbrowser.open('about:blank')
            speak("opening browser")

        elif 'open google chrome' in query:
            webbrowser.open("https://web.google chrome.com")
            speak("opening google chrome")

        elif 'shutdown pc' in query:
            print('okay')
            speak('okay')
            os.system('shutdown -s')

        elif 'email to nikunj' in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to="nikunjnasit90996@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry nikunj, i am not able to send this email")
        elif 'quit' in query:
            speak(" i  am , exit,  to the programe nikunj")
            exit()

        #elif 'open python shell' in query:
        #    codepath= "C:\\Users\\Paras\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\idle.pyw\\pythonw.exe"
        #    os.startfile(codepath)

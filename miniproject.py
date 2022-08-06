
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fileinput import filename
from http import server
import smtplib
import os
import time
import instaloader
#from tkinter import EXCEPTION
import PyPDF2
#from flask import request
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import cv2
import random
from requests import get
import pywhatkit as kit
import sys
import pyjokes
import pyautogui
import requests 
#import time



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

#Text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("Good evening")
    speak("I am  Prototype 1,how may i help you ")

#To convert voice into text
def takeCommand():      
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1
        #r.energy_threshold=200
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please")
        speak("Say that again please")
        return "None"
    return query

#def  sendEmail(to, content):
#    server=smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
#    server.starttls()
#    server.login('zakkiwork732.gmail.com','z@kkiworks786')
#    server.sendmail('zakkiwork732.gmail.com',to,content)
#    server.close() 
  

def news():
    #3801ee1289054d0b931574de41a92cd0
    main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3801ee1289054d0b931574de41a92cd0'
    main_page=requests.get(main_url).json() 
    #print(main_page)
    articles=main_page["articles"]
    #print(articles)
    head=[]
    day=["first","second","third","fourth","fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        #print(f"Today's {day[i]} nes is: {head[i]}")
        speak(f"Today's {day[i]} news is: {head[i]}")
    
def pdf_reader():
    book=open('Testing.pdf','rb')
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("Say the page number u want me to read")
    pg=int(input("Enter the page number u want me to read"))
    page=pdfreader.getPage(pg)
    text=page.extractText()
    speak(text)

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia..')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak("Sir,what should I search on google")
            gs=takeCommand().lower()
            webbrowser.open(f"{gs}")
       
        elif 'send message' in query:
            kit.sendwhatmsg("+918652336784","This message is send bt Prototype 1",14,2)

        elif 'play song on youtube' in query:
            kit.playonyt("Excuses Ap Dhillon")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
       
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
       
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
       
        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com")
        
        elif 'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"{ip} is your ip Address")
            print(f"{ip} is your ip Address")

        elif 'open camera' in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(20)
                if k==10:
                    break
            cap.release()
            cv2.destroyAllWindows()


        elif 'tell me a joke' in query:
            joke=pyjokes.get_jokes()
            speak(joke)

        elif 'tell me news' in query:
            speak('please wait sir, fetching the latest news')
            news()

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'play music' in query:
            Music_dir='C:\\Users\\JK\\Music\\Fav'
            songs=os.listdir(Music_dir)
            rd=random.choice(songs)
            #print(songs)
            os.startfile(os.path.join(Music_dir,rd))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir ,the time is{strTime}")

        elif 'open vs code' in query:
            codePath="C:\\Users\\JK\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath="C:\\Windows\\system32\\notepad.exe"
            os.startfile(codePath)

        elif 'where i am' in query or 'where we are' in query:
            speak('wait sir, let me check')
            try:
                ipAdd= requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_request=requests.get(url)
                geo_data=geo_request.json()
                #print(geo_data)
                city=geo_data['city']
                #state=geo_data['state']
                country=geo_data['country']
                speak(f"sir i am not sure,but I think we are in {city} of {country}")
            except Exception as e:
                speak('Sorry sir ,Due to network issue i am not able to find our location')
                
        elif 'instagram profile' in query or 'profile on instagram' in query:
            speak("Sir please enter the correct user name")
            name=input("enter the username")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            #time.sleep(5)
            speak("Sir would u like to download the profile pictrure of the account")
            condition=takeCommand().lower()
            if 'yes' in condition:
                mod=instaloader.Instaloader()
                mod.download_profile(name,profile_pic_only=True)
                speak("Done sir,profile picture is saved in your main folder")
            else:
                speak("Coulden't download")


        elif 'take screenshot' in query or 'take a screenshot' in query:
            speak('Please enter the name for this screenshot file')
            print('Please enter the name for this screenshot file')
            name=takeCommand().lower()
            speak("Please hold the screen for few seconds,I am taking screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Done sir,Anything else u want me to do")
                
        elif 'read pdf' in query:
            pdf_reader()



        elif 'close notepad' in query:
            speak("Okay sir,closing notepad")
            os.system("taskkill /f /im notepad.exe")
           
        elif 'set alarm' in query:
          alarm=int(datetime.datetime.now().hour)
          if alarm==22:
              music_dir='C:\\Users\\JK\\Music\\Fav'
              songs=os.listdir(music_dir)
              os.startfile(os.path.join(music_dir,songs[0])) 

     

        elif 'send email to' in query:
                speak("What should i say?")
                query=takeCommand().lower()
                if "send a file" in query:
                    email='zakkiworks732.gmail.com'
                    password='z@kkiworks786'
                    send_to_email="zakkiworks732.gmail.com"
                    speak("Sir what is the subject of the email")
                    query=takeCommand().lower()
                    subject=query # The subject in the email
                    speak("And what is the message for this email")
                    query2=takeCommand().lower()
                    message=query2 # the message in the email
                    speak("Please enter the correct path of the file here")
                    file_location=input("Please enter the path") #The file attachment in the email
                    speak("Please wait,I am sending email now")

                    msg=MIMEMultipart()
                    msg["from"]=email
                    msg["to"]=send_to_email
                    msg["subject"]=subject

                    msg.attach(MIMEText(message,'plain'))

                    #setup the attachment
                    filename=os.path.basename(file_location)
                    attachment=open(file_location,'rb')
                    part=MIMEBase('application','octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition","attachment; filename=%s"%filename)
                    
                    #attach the attachment to the multipart object
                    msg.attach(part)
                    server=smtplib.SMTP('smtp.gmail.com',587)
                    server.starttls()
                    server.login(email, password)
                    text=msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent ")
                else:
                    email='zakkiworks732.gmail.com'
                    password='z@kkiworks786'
                    send_to_email='zakkiworks732.gmail.com'
                    message=query
                    server=smtplib.SMTP('smtp.gmail.com',587)#connects to the server
                    server.starttls()#use tls
                    server.login(email, password)#login to the email server
                    server.sendmail(email, send_to_email, message)
                    server.quit()
                    speak('email has been sent')

         

        elif 'you can sleep' in query:
            speak("Thanks for using me sir,have a good day")
            print("Thanks for using me,have a good day")
            exit() 
        
        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")

        
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
    
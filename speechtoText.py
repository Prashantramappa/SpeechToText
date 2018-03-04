import speech_recognition as sr
from gtts import gTTS
from pygame import mixer
import os
import time
import winshell
import subprocess

def excel():
        os.system("start excel.exe")
def close_excel():
        os.system("taskkill /im excel.exe /f")

def devicemanager():
        os.system('C:\Windows\System32\devmgmt.msc')
def close_devicemanager():
        os.system("taskkill /f /im C:\Windows\System32\devmgmt.msc")

def CloseSpeechtoTextProgram():
         print("closing speech to Text Program")                  
        
##def lync():
  ##      os.system('start lync.exe')       
##def close_lync():
  ##      os.system("taskkill /f /im lync.exe")
        

##def open_outlook():
  ##      os.system("start outlook.exe")
       
##def close_outlook():
  ##      os.system("taskkill /F /IM OUTLOOK.EXE")
        

def check_ping():
    iplist=["255.255.255.0","191.168.1.1"]
    for ip in iplist:
        p = subprocess.Popen('ping '+ip,stdout=subprocess.PIPE)
        # the stdout=subprocess.PIPE will hide the output of the ping command
        p.wait()
        if p.poll():
            print (ip+" is down")
        else:
            print (ip+" is up")

            check_ping
##def notepad():     
##        os.system("start notepad.exe")
##def close_notepad():
##        os.system("taskkill /F /IM notepad.exe")

##def inventory():
        
  ##      os.startfile("C:\Users\inpcsm01\Desktop\HO Inventory on 22nd APR 16.xlsx - Shortcut.lnk")

def recyclebin():
        winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=True)
        

while True:

    r = sr.Recognizer()
    with sr.Microphone()as source:
            r.adjust_for_ambient_noise(source)
            print('Talk now: ')
            audio = r.listen(source)

    try:
        message = (r.recognize_google(audio))
        print(message)

        if 'hello' in message:
            speech = ('Hello Sir,How are you?')
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\hello.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\hello.mp3')
            mixer.music.play()

        if 'good morning' in message:
            speech = ('Good Morning Sir, ')
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\morning.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\morning.mp3')
            mixer.music.play()      

       
        if 'open Excel' in message:
            speech = (' OK Sir, ')
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\programexcel.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\programexcel.mp3')
            mixer.music.play()
            excel()

        if 'close Excel' in message:
            speech = ('Sure Sir, ')
            close_excel()
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\programcloseexcel.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\programcloseexcel.mp3')
            mixer.music.play()

        if 'IP Network' in message:
            speech = ('sure sir, ')
            check_ping()
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\programchecknetwork.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\programchecknetwork.mp3')
            mixer.music.play()

        if 'clean recycle bin' in message:
            speech = ('Cleaning recycle bin, ')
            recyclebin()
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\programrecyclebbin.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\programrecyclebin.mp3')
            mixer.music.play()

        if 'open device manager' in message:
            speech = ('sure sir, ')
            devicemanager()
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\programdevicemgr.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\programdevicemgr.mp3')
            mixer.music.play()

        if 'close device manager' in message:
            speech = ('sure sir, ')
            close_devicemanager()
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\programclsdevmgr.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\programclsdevmgr.mp3')
            mixer.music.play()
                     
        if 'Speech to Text Program Close' in message:
            speech = ('speech to text recording will be stopped, ')
            CloseSpeechtoTextProgram()
            tts = gTTS(text=speech, lang = 'en')
            tts.save('C:\\PGP_BABI\\speechtoText\\speechtoTextProgramclosed.mp3')
            mixer.init()
            mixer.music.load('C:\\PGP_BABI\\speechtoText\\speechtoTextProgramclosed.mp3')
            mixer.music.play()
            
    except Exception as e:
        print("Could not Understand" + e)
        
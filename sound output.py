import pyttsx3
import datetime
engine = pyttsx3.init()
def intro():
   engine.say("iam jarvis how can i help you")
   engine.runAndWait()
intro() 
def useinput():
   while True: 
    user=input("enter anything ").lower()
    if user=='hi'or user=="hello":
     engine.say("hello")
     engine.runAndWait()
    elif user=='how are you'or user=='how are u':
         engine.say("yea iam fine")
         engine.runAndWait()
    elif user=='how are you'or user=='how are u':
         engine.say("yea iam fine")
         engine.runAndWait()
    elif user=='what is time now'or user=='what is time now jarvis':
          x = datetime.datetime.now()
          H = (x.strftime("%I"))
          M = (x.strftime("%M"))
          p = (x.strftime("%p"))

          if int(H)<10 and int(M)<10:
             engine.say(H.strip("0"))          
             engine.runAndWait()
             engine.say(M.strip("0"))
             engine.runAndWait()
             engine.say(p)
             engine.runAndWait()
          elif int(H)<10 and int(M)>=10:
             engine.say(H.strip("0"))          
             engine.runAndWait()
             engine.say(M)
             engine.runAndWait()
             engine.say(p)
             engine.runAndWait()
          elif int(H)>=10 and int(M)<10:
             engine.say(H)          
             engine.runAndWait()
             engine.say(M.strip("0"))
             engine.runAndWait()
             engine.say(p)
             engine.runAndWait()
          else:
              engine.say(H)          
              engine.runAndWait()
              engine.say(M)
              engine.runAndWait()
              engine.say(p)
              engine.runAndWait()    

              
    else:
        engine.say("i can not understand")
        engine.runAndWait()
useinput()

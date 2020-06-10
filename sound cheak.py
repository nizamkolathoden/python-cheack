import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("speak")
    audio = r.listen(source)
    try:
      print("listn")
      txt = r.recognize_google(audio)
      print("you said : {}".format(txt))
    except:
        print("error")  
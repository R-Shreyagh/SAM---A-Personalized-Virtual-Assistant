import SpeechRecognition as sr
import pyttsx3 # for audio and text
import pywhatkit #to send msgs to whatsapp at certain time
import datetime
import wikipedia
listener = sr.Recognizer()
machine = pyttsx3.init()
def talk(text):
  machine.say(text)
machine.RAW() #run and wait
def input_instruction():
  global instruction
  try:
    with sr.Microphone() as origin:
      print("LISTENING")
      speech = listener.listen(origin)
      instruction = listener.recognize_google(speech)
      instruction = instruction.lower()
      if "SAM" in instruction:
        instruction = instruction.replace("SAM","")

        print(instruction)
      print(instruction)
  except:
    pass
    return instruction
def play_sam():
    instruction  = input_instruction
    print(instruction)
    if "PLAY" in instruction:
      song = instruction.replace("PLAY","")
      talk("PLAYING" +song)
      pywhatkit.playonyt(song)
    elif "TIME" in instruction:
      time = datetime.datetime.now().strftime("%I:%M&p")
      talk("Current time" + time)
    elif "DATE" in instruction:
      date = datetime.datetime.now().strftime("%d /%m /%y")
      talk("TODAY's DATE "+ date)
    elif "HOW ARE U" in instruction:
      talk("I AM FINE,HOW ABOUT U")
    elif "WHAT'S YOUR NAME" in instruction:
      talk("I AM SAM,HOW MAY I HELP U?")
    elif "WHAT IS" in instruction:
      datascience = instruction.replace("WHAT IS"," ")
      info = wikipedia.summary(datascience,1)
      talk(info)
    else:
      talk("PLEASE REPEAT")

play_sam()



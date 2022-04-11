import speech_recognition as sr
import pyttsx3
import datetime
import json

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

now = datetime.datetime.now()
day = "Wednesday"#now.strftime("%A")





def Take_Command():
    r1 = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        audio = r1.listen(source)
    try:
        print("Recognizing")
        query = r1.recognize_google(audio, language="en-in")
        print(f"User said {query}")

    except Exception as e:
        print("Say that again Please...... ")
        return None

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def load_json(query):
    f = open("schedule.json")
    data = json.load(f)

    Found = False
    if day == "Saturday" or day == "Sunday":
        speak(data[day])
        return
    for k in data[day]:


        if k == query:
            speak(data[day][k])
            Found = True
            break


    if Found == False:
        speak("Sorry couldn't find any lecture during this time duration ")


if __name__ == '__main__':

    q = Take_Command()
    load_json(q)

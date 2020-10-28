import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import wolframalpha
import requests
import subprocess
import pyttsx3
import re
from youtube_search import YoutubeSearch


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)
    print("Iris: " + text)
    engine.say(text)
    engine.runAndWait()


def openWord():
    speak('Opening Microsoft Word...')
    os.startfile(r'"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"')

def openExcel():
    speak('Opening Microsoft Excel...')
    os.startfile(r'"C:\Program Files\Microsoft Office\root\Office16/EXCEL.EXE"')

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("Your command: " + said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


def searchWiki(statement):
    wikipedia.set_lang("en")
    speak('Searching on Wikipedia...')
    speak('What do you want to know ?')
    command = get_audio()
    results = wikipedia.summary(command)
    speak("According to Wikipedia, " + results)

def note(text):
    date = datetime.datetime.now()
    filename= str(date).replace(":","-")+"-note.txt"
    with open(filename,"w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe",filename])

def wolframalpha():
    client = wolframalpha.Client("6GHTW8-6QGK95X58R")
    speak("What do you want to ask about ?")
    question = get_audio()
    res = client.query(question)
    speak(next(res.results).text)

def openWebsite(text):
    reg_ex = re.search("Open (.+)",text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'http://www.'+domain
        webbrowser.open(url)
        speak("The website you want is opened")
        return True
    else:
        return False

def readNews():
    speak("What do you want to listen about ?")
    queue=get_audio()
    params={
        'apiKey':'0868584bafbf4a03aa507fdc35379268',
        "q":queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?',params)
    api_response = api_result.json()
    speak("News")
    for number,result in enumerate(api_response['articles'],start=1):
        speak(f"""News number {number}:\nTitle: {result['title']}\nDescription: {result['description']}\nLink: {result['url']}
    """)

def playMusic():
    speak('What song do you want to play ?')
    mysong = get_audio()
    while True:
        result = YoutubeSearch(mysong,max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com/watch?v='+result[0]['id']
    webbrowser.open(url)
    speak('Done')

def weather():
    api_key="16786370ce79ed6754e737842b7c58f7"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    speak("What is the city name ?")
    city_name = get_audio()
    complete_url = base_url+"appid="+api_key+"&q="+city_name
    response= requests.get(complete_url)
    data=response.json()
    if data["cod"]!="404":
        city_res=data["main"]
        current_temp = city_res["temp"]
        current_humidity = city_res["humidity"]
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        speak("Temperature in kelvin unit is "+str(current_temp)+"\n humidity in percent is "+str(current_humidity)+"\n description is "+str(weather_description))
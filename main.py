from functions import *
if __name__ == '__main__':
    speak("Initial Loading...")
    WAKE = ['iris','hey iris','i need your help']
    STOP = ['turn off','stop','bye','goodbye']
    while True:
        statement = get_audio().lower()
        if statement==0:
            continue
        for phrase in WAKE:
            if phrase in statement:
                speak("What can I help you ?")
                statement =get_audio().lower()
                if 'wikipedia' in statement:
                    searchWiki(statement)
                if 'open word' in statement:
                    openWord()
                if 'open excel' in statement:
                    openExcel()
                if 'weather' in statement:
                    weather()
                if '.' in statement:
                    openWebsite(statement)
                if 'news' in statement:
                    readNews()
                if 'music' in statement:
                    playMusic()
                NOTE=['make a note', 'write this down', 'remember this']
                for phrase in NOTE:
                    if phrase in statement:
                        speak("What would you like me to note down ?")
                        note_text = get_audio()
                        note(note_text)
                        speak("I've made a note for that !")
                for phrase in STOP:
                    if phrase in statement:
                        speak("Always glad to help")
                        break
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

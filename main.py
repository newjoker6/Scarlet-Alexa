import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import randfacts
from pynput.keyboard import Key, Controller


listener = sr.Recognizer()
engine = pyttsx3.init()
assistant = 'scarlet'

keyboard = Controller()
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def run_assistant():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if assistant in command:
                print(command)
                command = command.replace(assistant, '', 1)
                if 'play' in command:
                    song = command.replace('play ', '', 1)
                    talk('playing' + song)
                    print(song)
                    pywhatkit.playonyt(song)
                elif 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('The time is ' + time)
                elif 'who is' in command or 'what is' in command:
                    print(command)
                    topic = command.replace('who is ', '', 1)
                    topic = command.replace('what is ', '', 1)
                    info = wikipedia.summary(topic, 1)
                    talk(info)
                elif 'joke' in command:
                    talk(pyjokes.get_joke())
                elif 'random fact' in command:
                    fact = randfacts.getFact()
                    talk(fact)
                    print(fact)
                elif 'refresh' in command:
                    keyboard.press(Key.f5)
                    keyboard.release(Key.f5)
                else:
                    print(command)
                    talk('I did not understand that please say again')
            else:
                pass
               # print(command)
               # talk('I did not understand that please say again')
    except:
        pass


while True:
    run_assistant()
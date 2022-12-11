# pip install PyAudio
# pip install fuzzywuzzy
# pip install pyttsx3
# pip install SpeechRecognition
# pip install rich
import os
import time
import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz
import datetime
import random
import sys
from time import sleep
from os import system
from colorama import *
import webbrowser
from rich.console import Console
from rich import print


console = Console(width=35)
style = 'bold white on blue'

# Name of all commands
commands = ['текущее время', 'сколько сейчас времени', 'который час',
            'открой браузер', 'открой диск C', 'сколько сейчас времени',
            'открой spotify', 'запусти youtube', 'открой ютуб', 'запусти браузер',
            'привет', 'команды', 'добрый день', 'здравствуй', 'пока',
            'выключи компьютер', 'выключи ПК', 'выруби компьютер', ]

r = sr.Recognizer()
engine = pyttsx3.init()
text = ''
j = 0
num_task = 0
r.pause_treshold = 0.5


def talk(speech):  # Voice output
    print(speech)
    engine.say(speech)
    engine.runAndWait()


def fuzzy_recognizer(rec):
    global j
    ans = ''
    for i in range(len(commands)):
        k = fuzz.ratio(rec, commands[i])
        if (k > 70) & (k > j):
            ans = commands[i]
            j = k
    return str(ans)


def listen():  # Text recognising
    global text
    text = ''
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(source=mic, duration=0.5)
        console.print('Code was modified by Kla1mzZ',
                      style=style, justify='center')
        print('Я вас слушаю')
        audio = r.listen(source=mic)
        try:
            text = r.recognize_google(audio, language="ru-RU").lower()
        except sr.UnknownValueError:
            pass
        system('cls')
        return text


def cmd_init():
    global text, num_task
    text = fuzzy_recognizer(text)
    print(text)
    if text in cmds:
        if (text != 'пока') & (text != 'привет') & (text != 'который час') & (text != 'сейчас времени')\
                & (text != 'сейчас времени') & (text != 'добрый день') & (text != 'здравствуй'):
            k = ['Сейчас']
            talk(random.choice(k))
        cmds[text]()
    elif text == '':
        talk("Я не поняла вашу команду")
    num_task += 1
    if num_task % 10 == 0:
        talk('У вас будут ещё задания?')
    engine.runAndWait()
    engine.stop()


def time():  # Says the time
    now = datetime.datetime.now()
    talk("Сейчас " + str(now.hour) + ":" + str(now.minute))


def open_browser():  # Opens the browser
    webbrowser.open('https://www.google.com')
    talk("Браузер открыт")


def help():  # Output all commands
    print(commands)


def open_youtube():
    webbrowser.open('https://www.youtube.com')
    talk("Ютуб открыт")


def open_spotify():
    os.startfile(
        'C:/Users/Мой ПК/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify')
    talk('Спотифай открыт')


def open_c():
    os.startfile('C:/')
    talk('Диск ц открыт')


def shut():  # Turns off PC
    system('shutdown /s /f /t 10')
    quite()


def hello():
    k = 'Привет, чем могу помочь?'
    talk(k)


def quite():  # Exit from voice assistent
    x = ['Надеюсь мы скоро увидимся',
         'Рада была помочь', 'Досвидания', 'До встречи']
    talk(random.choice(x))
    engine.stop()
    system('cls')
    sys.exit(0)


print(Fore.YELLOW + '', end='')
system('cls')


# run all commands
cmds = {
    # 'command': function name
    'текущее время': time, 'сколько сейчас времени': time, 'который час': time, 'открой диск C': open_c, 'открой spotify': open_spotify,
    'выключи ПК': shut, 'запусти youtube': open_youtube, 'открой youtube': open_youtube,
    'открой браузер': open_browser, 'команды': help, 'запусти браузер': open_browser, 'сколько сейчас времени': time,
    'привет': hello, 'добрый день': hello, 'здравствуй': hello,
    'пока': quite, 'вырубись': quite,
    'выключи компьютер': shut, 'выруби компьютер': shut,
}


def main():
    global text, j
    try:
        listen()
        if text != '':
            cmd_init()
            j = 0
    except UnboundLocalError:
        pass
    except NameError:
        pass
    except TypeError:
        pass


while True:
    main()

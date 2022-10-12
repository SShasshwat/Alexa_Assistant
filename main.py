import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()      # To recognize user's voice
engine = pyttsx3.init()         # Engine that will speak to you
voices = engine.getProperty('voices')           # To set all python voice in voices
engine.setProperty('voice', voices[1].id)       # To get the second voice from all the voice # To convert voice to female voice

def talk(text):         # Alexa to speak the text
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:         # To use mic as source of audio
            print('listening...')               # When this is printed then Alexa is ready to listen the command
            voice = listener.listen(source)     # To listen to that source
            command = listener.recognize_google(voice)      # Google API to convert audio to text
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')      # To remove word Alexa from command
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)     # 1 is passed to get 1 line of result
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())        # If user want to listen joke
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
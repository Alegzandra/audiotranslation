import googletrans
from googletrans import Translator
import pyttsx3
import speech_recognition as sr


r = sr.Recognizer()
mic = sr.Microphone()

print('Say something')

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    result = r.recognize_google(audio, language = 'ro-RO', show_all = True)

    try:
        print(result)
    except:                            # speech is unintelligible
        print("Could not understand audio")


# definire translator
p = Translator()

# preluare text din result
result_values = []
for value in result.values():
    result_values.append(value)
values_view = result_values[0][0].values()
value_iterator = iter(values_view)
text_de_tradus = next(value_iterator)

print('Textul pentru traducere:', text_de_tradus)
k = p.translate(text_de_tradus, dest='en')
print(k, type(k))
print('Textul tradus:', k.text)

translated = k.text

# definire text-to-speech engine
engine = pyttsx3.init()

# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#

engine.setProperty('voice', 'english') #se trece explicit limba corespondenta traducerii de la p.translate

engine.say(translated)

#engine.save_to_file(translated, 'output.mp3')

engine.runAndWait()

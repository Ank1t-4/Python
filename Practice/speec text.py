#text to speech
import win32com.client
string_to_speak=input("Enter the string to speak: ")
string_to_speak_list=string_to_speak.split()
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak(string_to_speak_list)



#speech to text
import speech_recognition as sr
from speech_recognition.recognizers import google, whisper

r = sr.Recognizer()

audio_file = sr.AudioFile("C:/Users/nothi/Downloads/WhatsApp Audio 2024-11-22 at 20.58.46_eb49b551.wav")

with audio_file as source:

 audio = r.listen(source)

text = r.recognize_google_cloud(audio)

print(text)
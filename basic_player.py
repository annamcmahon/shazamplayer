#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import os
from pygame import mixer 
import time
os.system("say sing me a song")

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)


mixer.init()
# Speech recognition using Google Speech Recognition
try:
	audioText = r.recognize_google(audio)
	print audioText
	audioText = audioText.lower()
	audioWords = audioText.split()
	if "sugar" in audioWords:
		#os.system("spotify play Sugar") # works if you have: https://github.com/hnarayanan/shpotify
		mixer.music.load('sugar.mp3')
		mixer.music.play(loops=-1)
		while mixer.music.get_busy() == True:
			continue
	else:
		os.system("say I cannot " + audioText)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

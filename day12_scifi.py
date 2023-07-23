#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import time
import subprocess
import json


# In[3]:


import wolframalpha
import wikipedia
import requests
import webbrowser
import datetime


# In[4]:


import speech_recognition as sr
import pyttsx3


# In[5]:


print('LOADING YOUR AI PERSONAL ASSISTANT JARVIS')


# In[6]:


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')


# In[7]:


def speak(text):
    engine.say(text)
    engine.runAndWait()


# In[8]:


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak('hello, good morning mr.abc')
        print('hello, good morning mr.abc')
    elif hour >= 12 and hour <= 18:
        speak('hello, good afternoon mr.abc')
        print('hello, good afternoon mr.abc')
    else:
        speak('its already the night time better go to sleep')
        print('its already the night time better go to sleep')


# In[9]:


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('i am listening')
        audio = r.listen(source)
        
        try:
            statement = r.recognize_google(audio, language='eng-in')
            print(f'user said:{statement}\n')
            
        except Exeception as e:
            speak('pardon me, please say that again')
            return 'None'
        return statement


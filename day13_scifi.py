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


# In[11]:


speak('LOADING YOUR AI PERSONAL ASSISTANT JARVIS ')
wishMe()


# In[ ]:


if__name__ == '__main__':
    while True:
        speak('how can i help you?')
        statement = takeCommand().lower()
        if statement == 0:
            continue
            if 'goodbye' in statement or 'ok bye' in statement or 'stop' in statement:
                speak('your personal ai assistant jarvis is shutting down, goodbye')
                print('your personal ai assistant jarvis is shutting down, goodbye')
                break
                
            if 'wikipedia' in statement:
                speak('searching wikipedia........')
                statement = statement.replace('wikipedia','')
                results = wikipedia.summary(statement, sentences = 3)
                speak('according to wikipedia......')
                print(results)
                speak(results)
                
            elif 'open youtube' in statement:
                webbrowser.open_new_tab('https://www.youtube.com')
                speak('youtube is open for u')
                time.sleep(5)
                
            elif 'open google' in statement:
                webbrowser.open_new_tab('https://www.google.com')
                speak('google search is open for u')
                time.sleep(5)
                
            elif 'open gmail' in statement:
                webbrowser.open_new_tab('gmail.com')
                speak('your gmail is open for u')
                time.sleep(5)
                
            elif 'weather' in statement:
                api_key='8ef61edc576d65d836254e11ea420'
                base_url = 'https://api.openweathermap.org/data/2.5/weather?'
                speak('whats city name')
                city_name = takeCommand()
                complete_url = base_url + 'appid = '+api_key+'&q='+city_name
                response = requests.get(complete_url)
                x = response.json()


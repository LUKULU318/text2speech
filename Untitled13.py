#!/usr/bin/env python
# coding: utf-8

# In[3]:


from gtts import gTTS
import os
import pygame

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)
    print(f"Audio saved as {audio_file}")
    
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio file
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)

from gtts import gTTS
import os
import pygame

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)
    print(f"Audio saved as {audio_file}")
    
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio file
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        continue

if __name__ == "__main__":
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)



# In[ ]:





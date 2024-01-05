# GnAIChatUI.py

import speech_recognition as sr
import pyttsx3
import os
import constants as c
import time
import pygame
from gtts import gTTS
import Voice_Tools3 as v
import Skill_Launch as sl
import llama_index
myquestion = ''

# wait for wake word
while myquestion != 'exit':
  wakeword = v.Check_For_Wakeword()
  woken = v.Phrase_Exists(wakeword, "Matrix")
  if woken == True:
    wakeword = ''
    print('woken')
    quest = v.Ask_Voice_Question()
    if sl.Check_If_Skill(quest) == False:
      answer = chatbot(quest, index)
      print(answer)
      v.Play_Prompt(answer, 'response', 'speak')
    else:
      print(quest)
      sl.Run_Skill(quest)
  else:
    pass

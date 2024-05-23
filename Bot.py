import flet as ft
import os
import sys
import speech_recognition as sr
from hugchat import hugchat
import time
import pyttsx3
import speech_recognition 
import pyautogui as autogui

def main(page: ft.Page):
    page.window_width = 400        
    page.window_height = 400
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = False  

    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.setProperty("rate", 170)

    chatbot = hugchat.ChatBot(cookie_path="cookies.json")

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    def button_click(btn):  
        while True:
            chatBot()

    def chatBot():
        try:
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            try:
                print("Recognizing...")
                user_input = recognizer.recognize_google(audio, language="en-US")
                print("You said:", user_input)
            except sr.UnknownValueError:
                print("Sorry, could not understand audio.")
                return
            except sr.RequestError as e:
                print("Sorry, could not request results. Check your internet connection.")
                return

            user_input = user_input.lower()
            response = chatbot.chat(user_input) 
            print(response)
            speak(response)
            # speak(response)

            # Check if the user wants to quit the conversation
            if user_input == "quit":
                sys.exit() 

        except sr.RequestError as e:
            print(f"Error: {e}")




    

    btn = ft.ElevatedButton("Start!", on_click=button_click)

    page.controls.append(btn)
    page.update()

ft.app(target=main)

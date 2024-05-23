import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("Say something! (or say 'exit' to quit)")

    while True:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")

            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()

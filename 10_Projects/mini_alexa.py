#pip install speechrecognition 
#pip install pyttsx3 
#pip install wikipedia
#pip install pyjokes
#pip install pyaudio

import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes

# Initializing the text-to-speech engine
engine = pyttsx3.init()

# Function to make Alexa speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take voice command
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # seconds to wait before stopping
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that. Please repeat.")
        return "none"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "none"
    return query.lower()

# Main program
def main():
    speak("Hello! I am your Mini Alexa. How can I help you today?")

    while True:
        query = take_command()

        if query == "none":
            continue

        # Greet
        if "hello" in query:
            speak("Hello! How are you?")

        # Time
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        # Date
        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {date}")

        # Open Google
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # Open YouTube
        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        # Wikipedia Search
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        # Joke
        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        # Exit
        elif "stop" in query or "exit" in query:
            speak("Goodbye! Have a nice day.")
            break

        # Unknown command
        else:
            speak("Sorry, I can't do that yet.")

if __name__ == "__main__":

    main()

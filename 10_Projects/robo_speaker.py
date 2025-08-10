import pyttsx3

def main():
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    
    print("I am Robo Speaker version 1.0!!")
    
    while True:
        speak = input("Tell me something: ")
        
        if speak.lower() == "bye robo":
            print("Bye Bye Friend.....!!")
            engine.say("Bye Bye Friend.....!!")
            engine.runAndWait()
            break
        
        engine.say(speak)
        engine.runAndWait()
            

if __name__ == "__main__":
    main()
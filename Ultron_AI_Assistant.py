# Ultron - (AI Assistant).
# This AI assistant tells us date ,time, weather; open websites like google,chatgpt,youtube,instagram also search anything for you on google.

# First we install and import all modules and built-in modules that will help us to do such things.
import speech_recognition            # Help us to convert our voice to text.
import pyttsx3                       # Help us to convert text to voice.
import pyaudio                       # Help us to access our voice through microphone.
import requests                      # Help us to access data from websites like weather,news,etc.
import webbrowser                    # Help us to open websites like google,chatgpt,youtube,instagram (Built-in module).
from datetime import datetime        # Help us to know current date and time (Build in module).

# Now we start the engine of pyttsx3.
engine = pyttsx3.init() 
engine.setProperty('rate',150)                  # Speech of voice.
engine.setProperty('volume',1)                  # volume of voice.
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)        # Here we set the voice of male [0] and for female is [1].

# Now we make a speak program function to ultron to talk.
def speak(text):
    print("Ultron:",text)
    engine.say(text)
    engine.runAndWait()                        # Here ultron starts speaking.

# Now we make the listen program function to make ultron listen to me.
def listen():

    r = speech_recognition.Recognizer()                      # This will process our voice.
    with speech_recognition.Microphone() as source:          # This will take our microphone real time voice as a input.
        print("Ultron: Listening....")                       # Here it prints that.
        audio = r.listen(source)                             # Here it records our voice.

    try:
        command = r.recognize_google(audio)                  # Here it sends our voice to google.
        print(f"You said:{command}")
        return command.lower()
        
    except:
        speak("Sorry sir, I didn't understand what you have said.")
        speak("Please tell again sir.")
        return ""
    
# Now we add a program function of current date and time for ultron.
def say_date_time():

    now = datetime.now()

    time = now.strftime("%I:%M %p")         # This tells current time.
    date = now.strftime("%d-%b-%Y")         # This tells current date.

    try:
        print(f"The current time is:{time} and the date is:{date}.")          
        speak(f"As of now sir,The time is:{time} and the date is:{date}.")

# If due to some reasons ultron can't access the time and date instead of crashing the program it will print this.

    except:
        speak("Sorry sir, I can't access the current time and date now.")     
        speak("Please try again.")

# Now we add a program function of weather for ultron.
def tell_weather():
    speak("Which city weather you want to know sir?")
    city = listen()
    
    try:
        weather = requests.get(f"https://wttr.in/{city}").text          # This code tells the weather.
        speak(f"Sir, The weather in city:{city} is: {weather}")
    
    except:
        speak("Sorry sir, Due to some reasons i can't access the weather right now.")
        speak("Try again later.")

# Now we add a function program for google search so ultron can search anything on google itself.
def search_google():
   
    query = listen()

    try:
        speak(f"Searching for {query} sir....")
        webbrowser.open(f"https://www.google.com/search?q={query}")          # q is the official way to search on google through url.

    except:
        speak("Sorry sir, I didn't hear what you said.")
        speak("Please say again sir.")

# Now we add a function program for opening google for ultron.
def open_google():

    try:
        speak("Opening google sir....")
        webbrowser.open("https://www.google.com")            # This will open google.

    except:
        speak("Can't open google right now.")
        speak("Please try again later sir.")

# Now we add a function program for opening chatgpt for ultron.
def open_chatgpt():

    try:
        speak("Opening chatgpt sir....")
        webbrowser.open("https://chat.openai.com")            # This will open chatgpt.

    except:
        speak("Can't open chatgpt right now.")
        speak("Please try again later sir.")

# Now we add a function program for opening youtube for ultron.
def open_youtube():

    try:
        speak("Opening youtube sir....")
        webbrowser.open("https://www.youtube.com")            # This will open youtube.

    except:
        speak("Can't open youtube right now.")
        speak("Please try again later sir.")

# Now we add a function program for opening instagram for ultron.
def open_instagram():

    try:
        speak("Opening instagram sir....")
        webbrowser.open("https://www.instagram.com")            # This will open instagram.

    except:
        speak("Can't open instagram right now.")
        speak("Please try again later sir.")

# Now we add the final loop function to work all these functions for ultron.
if __name__ == "__main__":                                          # This functions protects code from direct running.
    speak("Initializing ultron sir....")
    speak("I am here to assist you and to help you.")
    speak("For now how may i help you?")

while True:
    command = listen()                                                           # Here we creates an infinite loop.
    
    if "time" in command or "date" in command:
        say_date_time()

    elif "weather" in command:
        tell_weather()

    elif "search google" in command and "open google" not in command:
        search_google()

    elif "open google" in command:
        open_google()

    elif "open chatgpt" in command:
        open_chatgpt()

    elif "open youtube" in command:
        open_youtube()

    elif "open instagram" in command:
        open_instagram()

    elif "stop" in command or "bye" in command:
        speak("Ok sir Goodbye for now....")
        speak("See you soon sir, take care.")
        break                                                          # Here we breaks the infinite loop.


# Now the program finally ends.
# In future we will add more functions and made this more advanced.






    



    



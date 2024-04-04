# pip install SpeechRecognition
# pip install pyaudio ->for dealing with speakers/microphone
# pip install pyttsx3

import speech_recognition as sr
import os
from datetime import datetime   
import webbrowser
import time
import pyttsx3



engine= pyttsx3.init() #'sapi5'
voices = engine.getProperty('voices')
# # checking availiable voices in windows system->david(male) and zira(female) found
# for voice in voices:
#     print("Voice:")
#     print(" - ID: %s" % voice.id)
#     print(" - Name: %s" % voice.name)

engine.setProperty('voice', voices[1].id) #set zira as default
# Change speaking rate (default is 200)
engine.setProperty('rate', 150)




# *.............................speak...............................................

def speak(text):
    engine.say(text) # Convert text to speech
    engine.runAndWait() # Play the speech



# # Save speech to a WAV file
# engine.save_to_file(text, 'output.wav')
# engine.runAndWait()



# *................................SpeechToText..............................................

def SpeechToText():
    recognizer = sr.Recognizer() #create a recognizer object

    with sr.Microphone() as source:  #set souurcse of audio as microphone
        print("Capturing ambient noise from the microphone (background noise)")
        recognizer.adjust_for_ambient_noise(source,duration=3) #this will capture the background noise so to adjust the adjust the recognizer's sensitivity. 
        print('Now Say Something...')
        audio= recognizer.listen(source,timeout=3) #listen to microphone with the timeout of 3sec means that it detects speech within that time,it will continue to capture until there is a pause in speech. If no speech is detected within the 3 seconds, it will stop capturing audio and proceed to the next step.
        print("Recognizing...")

    try:
        # calling Google Web Speech API to transcribe the captured audio data into text
        text= recognizer.recognize_google(audio,language="en-in")
        print("You said...", text)


    except Exception as e:
        # print('Error : ', str(e))
        print("Could you please say it again")
        speak("Could you please say it again")




# *..........................speechToTextAndSaveInAudioFile...........................

def speechToTextAndSaveInAudioFile():
    recognizer = sr.Recognizer() #create a recognizer object

    with sr.Microphone() as source:  #set souurcse of audio as microphone
        print("Capturing ambient noise from the microphone (background noise)")
        recognizer.adjust_for_ambient_noise(source,duration=3) #this will capture the background noise so to adjust the adjust the recognizer's sensitivity. 
        print('Now Say Somethong...')
        audio= recognizer.listen(source,timeout=3) #listen to microphone with the timeout of 3sec means that it detects speech within that time,it will continue to capture until there is a pause in speech If no speech is detected within the 3 seconds, it will stop capturing audio and proceed to the next step.
        print("Recognizing...")

    try:
        # calling Google Web Speech API to transcribe the captured audio data into text
        text= recognizer.recognize_google(audio,language="en-in")
        print("You said...", text)

        # Create the AudioFiles folder if it doesn't exist
        folderName = "AudioFiles"
        os.makedirs(folderName, exist_ok=True)

        # Generate a filename with date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        audioFileName = f"speech_audio_{current_datetime}.wav"#for unique naming

        audioFilePath= os.path.join(folderName, audioFileName)#concatinate->/

        with open(audioFilePath, "wb") as f:#write in binary
            f.write(audio.get_wav_data())

        print(f"Audio saved as {audioFilePath}")

    except Exception as e:
        # print('Error : ', str(e))
        print("Could you please say it again")
        speak("Could you please say it again")




# *............................recordedAudioToText...............................


def recordedAudioToText():
    recognizer = sr.Recognizer() #create a recognizer object

    audiofilePath= "AudioFiles\speech_audio_2023-09-07_11-09-35.wav"

    with sr.AudioFile(audiofilePath) as source:  #set souurcse of audio as audioFile

        audio= recognizer.record(source)
        print("Recognizing...")

    try:
        # calling Google Web Speech API to transcribe the captured audio data into text
        text= recognizer.recognize_google(audio,language="en-in")
        print("Text from audio:...", text)


    except Exception as e:
        #  print('Error : ', str(e))
        print("Could you please say it again")
        speak("Could you please say it again")






# *............................speakToOpenWebsites...............................

def speakToOpenWebsites():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Capturing ambient noise from the microphone (background noise)")
        r.adjust_for_ambient_noise(source,duration=3)

        print("Say 'Open' followed by the website name...")

        audio= r.listen(source)

        print("Recognizing...")

    try:
        command= r.recognize_google(audio,language="en-in").lower()
        print(f'You said {command}')

        if "open" in command: #open youtube
            # Extract the website name
            # command.split("open")->['', ' youtube']
            websiteName= command.split("open")[1].strip() or command.split("open")[0].strip() 
            website = "https://" + websiteName

            if ".com" in website:
                pass
            else:
                website= website.strip() + ".com"

            print(f"Opening {website} in your default web browser.")
            speak(f"opening {websiteName.capitalize()} in your default web browser")
            # time.sleep(1)

            webbrowser.open(website)

        else:
            print(f"The Command you provided doesn't have 'open' phrase")
            speak(f"The Command you provided doesn't have 'open' phrase")
            speakToOpenWebsites()

    except Exception as e:
        # print('Error : ', str(e))
        print("Could you please say it again")
        speak("Could you please say it again")
        speakToOpenWebsites()
            




        


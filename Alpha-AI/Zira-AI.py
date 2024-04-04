import win32com.client as wincl #use to acces the COM functionility
import speech_recognition as sr
import datetime
import webbrowser
import os
import openai



# ......................Setting the voice to female(zira)...................
speaker = wincl.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
# for voice in voices:
#     print(f"Voice Name: {voice.GetDescription()}")
speaker.Voice = voices[1]



def say(text):
    speaker.Speak(text)


def takeCommand():
    r= sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio= r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Please say it again!"
        



def wishMe():
    hour = int (datetime . datetime.now(). hour )
    if hour>=0 and hour<12:
        say("Good Morning!")
    elif hour>=12 and hour<18:
        say("Good Afternoon!")
    else:
        say("Good Evening!")

    say("Hi,I am Zira AI,How may i help You")



def openWebsite(command):
    websiteName= command.split("open")[1].strip() or command.split("open")[0].strip() 
    website = "https://" + websiteName

    if ".com" in website:
                pass
    else:
        website= website.strip() + ".com"

    say(f"opening {websiteName}")
    # time.sleep(1)

    webbrowser.open(website)


# def ai(prompt):
#     openai.api_key = "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"
#     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

#     try:
#         response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=prompt,
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#         )

#         text += response["choices"][0]["text"]
#         if not os.path.exists("Openai"):
#             os.mkdir("Openai")

#         with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
#             f.write(text)

    # except Exception as e:
    #     print(str(e))
    #     say("please say it again")



# print(__name__)
# the below code is executed only when this file is run directly and if it is imported then the __name__ changes to that file name so the condition will not be stisfied so no execution of below code in other file....
if __name__== '__main__':
    print('Welcome to Zira A.I')
    wishMe()

    while True:
        print("Listening...")
        query = takeCommand()

        apps=[
            ["Visual Studio code","C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
              ["Postman","C:\\Users\\Dell\\AppData\\Local\\Postman\\Postman.exe"],
              ["word", "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"],
            ]
        found=False
        
        if "open" in query.lower():
            for app in apps:
                if f"{app[0]}".lower() in query.lower():
                    say(f"Opening {app[0]} sir...")
                    os.startfile(app[1])
                    # print("app")
                    found=True
                    

            
            if not(found):
                openWebsite(query)
                exit()
                # print("web")
            
            exit()

        elif "time" in query.lower():
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours and {min} minutes")

        # elif "how" or "when" or "who" or "what" or "where" or "why" or "how" or "can" or "do" or "is" in query.lower():
        #     ai(prompt=query)



        
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
# from nltk.tokenize import word_tokenize

# Initialize the Tkinter window
root = tk.Tk()
root.title("Speech to English Sentence")

# Initialize the speech recognition recognizer
recognizer = sr.Recognizer()

# Function to convert audio to text
def convert_audio_to_text():
    try:
        with sr.Microphone() as source:
            print("Listening...")            
            audio = recognizer.listen(source)
            print("Audio input captured.")
            
        
        # Use NLTK for tokenization and display the result
        text = recognizer.recognize_google(audio)
        # tokens = word_tokenize(text)
        result_label.config(text="English Sentence: " + text,background='white',foreground='black',font='arial')
    except sr.UnknownValueError:
        result_label.config(text="Could not understand audio.")
    except sr.RequestError as e:
        result_label.config(text=f"Could not request results; {e}")

# Create and configure the GUI components
info_label = ttk.Label(root, text="Press the button and speak.")
info_label.pack(pady=10)

start_button = ttk.Button(root, text="Start Recording", command=convert_audio_to_text)
start_button.pack()

result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
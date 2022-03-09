import tkinter as tk
from tkinter import filedialog, Text
import os
from pydub import AudioSegment
from pathlib import Path
from speech_recognition import Recognizer, AudioFile
import nltk

nltk.download('vader_lexicon')
nltk.download('twitter_samples')
from nltk.sentiment import SentimentIntensityAnalyzer
#design the app
root = tk.Tk()
canvas = tk.Canvas(root, height=350, width=350, bg='#263D42')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

openfile = tk.Button(root, text='Open File', padx=10, pady=5, fg='white', bg='#263D42')
openfile.pack()

analyze = tk.Button(root, text='Mood', padx=10, pady=5, fg='white', bg='#263D42')
analyze.pack()

root.mainloop()
#upload audio file
#turn audio file to text
#analyze the words and show the result

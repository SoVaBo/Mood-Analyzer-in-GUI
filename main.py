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
#upload audio file
#turn audio file to text
#analyze the words and show the result
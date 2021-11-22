# import numpy as np
# import pywhatkit
from pytube import YouTube
link = input("Please enter the link")
print("Downloading")
YouTube(link).streams.filter(res="720p").first().download()
print("Vid is successfully downloaded")

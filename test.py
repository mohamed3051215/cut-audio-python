import sys
import os
from pydub import AudioSegment
print(str(sys.path))

dir_path = os.path.dirname(os.path.realpath(__file__))
print("current working dir: %s" % dir_path)

sys.path.insert(0, dir_path)
AudioSegment.converter = os.getcwd()+ "\\ffmpeg\\bin\\ffmpeg.exe"                    
AudioSegment.probe   = os.getcwd()+ "\\ffmpeg\\bin\\ffprobe.exe"
audio = AudioSegment.from_file('music.mp3' , format="mp3")
exported = audio[6000:7000]
exported.export("music_new.mp3", format="mp3")
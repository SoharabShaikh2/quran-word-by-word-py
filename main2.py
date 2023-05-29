



import moviepy.editor
import numpy as np
import bidi

import arabic_reshaper
from bidi.algorithm import get_display



from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.segmenting import findObjects

#clip1 = VideoFileClip("back.mp4").subclip(1,2)
#combined = clip1.subclip(0, 2)
#combined.write_videofile("newfile.mp4")


# Import everything needed to edit video clips

# loading video file clip
clip = VideoFileClip("back.mp4")

# clipping of the video
# getting video for only starting 10 seconds

#clip = clip.subclip(0, 5)

# Reduce the audio volume (volume x 0.5)

#clip = clip.volumex(0.5)

# Generate a text clip
def formatArabicSentences(sentences):
   formatedSentences = arabic_reshaper.reshape(sentences)
   return get_display(formatedSentences)


txt_clip = TextClip("بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ", fontsize=125, color='white')

# setting position of text in the center and duration will be 5 seconds
txt_clip = txt_clip.set_pos('center').set_duration(0, 10)


txt_clip1 = TextClip("بِسۡمِِ", fontsize=125, color='white')
txt_clip1 = txt_clip1.set_pos('center').set_duration(10, 15)

txt_clip2 = TextClip("ٱللَّهِِ", fontsize=125, color='white')
txt_clip2 = txt_clip2.set_pos('center').set_duration(15, 20)

txt_clip3 = TextClip("ٱلرَّحۡمَٰنِِ", fontsize=125, color='white')
txt_clip3 = txt_clip3.set_pos('center').set_duration(20, 25)

txt_clip4 = TextClip("ٱلرَّحِيمِ", fontsize=125, color='white')
txt_clip4 = txt_clip4.set_pos('center').set_duration(25, 30)


# Overlay the text clip on the first video clip
video = CompositeVideoClip([clip, txt_clip, txt_clip1, txt_clip2, txt_clip3, txt_clip4])

# showing video
video.write_videofile("newfile.mp4")


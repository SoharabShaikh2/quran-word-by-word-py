import moviepy.video.fx.all as vfx
import json

from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.volumex import volumex
from moviepy.audio.io.AudioFileClip import AudioFileClip

from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip


# for i in data["wbw"]:
# print(i)

# print(jsonData)


def convertAyatToVideo():
    screensize = (980, 1860)
    clip = VideoFileClip("back.mp4", audio=False)

    txt_clip2 = TextClip("bengali", font='Bangla.ttc', fontsize=100, color='white', align='center',
                         size=screensize, method='caption')
    txt_clip2 = txt_clip2.set_position('center').set_duration(10).set_start(0)
    txt_clip2 = vfx.fadein(txt_clip2, 1)
    txt_clip2 = vfx.fadeout(txt_clip2, 0.5)

    video = CompositeVideoClip([txt_clip2])
    # showing video
    video.write_videofile("video.mp4")




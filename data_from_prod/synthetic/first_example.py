# Import everything needed to edit video clips
from moviepy.editor import *

# Load video1
clip1 = VideoFileClip("ig_15secs.mov").subclip(0,15)

# Reduce the audio volume (volume x 0.0)
clip1 = clip1.volumex(0.0)

# # Load video2
# clip2 = VideoFileClip("v2.mp4").subclip(0,10)
#
# # Reduce the audio volume (volume x 0.0)
# clip2 = clip2.volumex(0.0)

# Generate a text clip. You can customize the font, color, etc.
txt_clip = TextClip("Baidu News Short Video",fontsize=30,color='red')

# Say that you want it to appear 10s at the center of the screen
txt_clip = txt_clip.set_pos('bottom').set_duration(5)

# # add images
# my_clip2 = ImageClip("p2.png") # has infinite duration
# my_clip2.set_duration(5)#.write_videofile("p2.mp4") # works !
#
# my_clip3 = ImageClip("p3.png") # has infinite duration
# my_clip3.set_duration(5)#.write_videofile("p3.mp4") # works !


img = ['p0.png', 'p1.png','p2.png', 'p3.png']

clips = [ImageClip(m).set_duration(5) for m in img]
clips.append(clip1)

audioclip = AudioFileClip("ig_34sec.mp3")
concat_clip = concatenate_videoclips(clips, method="compose").set_audio(audioclip.set_duration(33))
concat_clip.write_videofile('ig_champion.webm',fps=25)


# clipISC = ImageSequenceClip(['p2.png', 'p3.png'], fps=24)
# video = CompositeVideoClip([clips])
# video.write_videofile("CompositeVideoClip.mp4")


compo = CompositeAudioClip([audioclip.volumex(1.2)])

final_clip = concatenate_videoclips([clip1]).set_audio(audioclip.set_duration(clip1.duration))

# concat_clip.write_videofile("test.mp4")

# print '\nfinal:\n'
#
# # Overlay the text clip on the first video clip
video = CompositeVideoClip([final_clip, txt_clip])
# video = video.set_audio(compo.set_duration(20))
#
# # Write the result to a file (many options available !)
video.write_videofile("output.mp4")



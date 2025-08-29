import moviepy.editor as mp
from gtts import gTTS

def generate_video(script: str, output="output.mp4"):
    # Narration
    tts = gTTS(text=script, lang="en")
    tts.save("narration.mp3")

    # Placeholder video (black background)
    clip = mp.ColorClip(size=(1280,720), color=(0,0,0), duration=30)

    # Add audio
    audio = mp.AudioFileClip("narration.mp3")
    clip = clip.set_audio(audio)

    # Export
    clip.write_videofile(output, fps=24)
    return output

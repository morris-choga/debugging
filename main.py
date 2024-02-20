
import time

from moviepy.editor import *
from pytube import YouTube
import os

from pytube.exceptions import PytubeError
count = 1

def download(title,video_id,location):
    link = f'https://music.youtube.com/watch?v={video_id}'

    try:

        yt = YouTube(link)
        yt.title = "".join([c for c in yt.title if c not in ['/', '\\', '|', '?', '*', ':', '>', '<', '"']])
        video = yt.streams.filter(only_audio=True).first()
        vid_file = video.download(output_path=location)
        base = os.path.splitext(vid_file)[0]
        audio_file = base + ".mp3"

    except Exception as e:
        print(f"Error has occured with ytmusicapi: {str(e)}")
        return f"Error has occured with ytmusicapi: {str(e)}"


    try:

        mp4_no_frame = AudioFileClip(vid_file)
        mp4_no_frame.write_audiofile(audio_file, logger=None)
        mp4_no_frame.close()
        os.remove(vid_file)
        os.replace(audio_file, location + "/" + yt.title + f" {count}.mp3")
        audio_file = location + "/" + yt.title + ".mp3"
        return audio_file


    except PytubeError as e:
        print(f"An error occured with PytubeError: " + str(e))
        return f"An error occured with PytubeError: " + str(e)

    except Exception as e:
        print(f"Error has occured: {str(e)}")
        return f"Error has occured: {str(e)}"




while count<5:

    download(f"Not Afraid {str(count)}", "-grPV-Fae6I", "/songs")
    # download(f"Not Afraid {str(count)}", "-grPV-Fae6I", "C:\\Users\\Mchog\\Desktop\\dockersongs")

    time.sleep(6)
    count+=1
    print("downloaded")




import paramiko
import time

from moviepy.editor import *
from pytube import YouTube
import os

from pytube.exceptions import PytubeError
count = 0

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





from ftplib import FTP


def upload_file_via_ftp(local_path, remote_path, ftp_host, ftp_user, ftp_pass):
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    with open(local_path, 'rb') as file:
        ftp.storbinary(f'STOR {remote_path}', file)

    ftp.quit()


# Example usage
local_file_path = f'{os.getcwd()}/Not Afraid '
remote_file_path = f'/songs/Not Afraid'
ftp_host = '162.251.120.221'
ftp_user = 'eminem'
ftp_pass = '10361036'

while True:

    download(f"Not Afraid {str(count)}", "-grPV-Fae6I", os.getcwd())
    upload_file_via_ftp(f"{local_file_path}{str(count)}.mp3", f"{remote_file_path} {str(count)}.mp3", ftp_host, ftp_user, ftp_pass)
    count+=1
    time.sleep(5)
    print(count)




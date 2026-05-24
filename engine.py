import os
import ffmpeg
import yt_dlp
from qbittorrentapi import Client

# إعداد التورنت
qb = Client(host='http://127.0.0.1', port=8080, username='admin', password='password')

def compress_video(input_file, resolution="720"):
    output_file = f"compressed_{resolution}.mp4"
    scale_map = {"360": "640:-2", "480": "854:-2", "720": "1280:-2", "1080": "1920:-2"}
    stream = ffmpeg.input(input_file).output(output_file, vcodec='libx265', crf=28, vf=f"scale={scale_map[resolution]}", acodec='aac')
    ffmpeg.run(stream, overwrite_output=True)
    return output_file

def download_video(url):
    ydl_opts = {'format': 'best', 'outtmpl': 'input.mp4'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return "input.mp4"

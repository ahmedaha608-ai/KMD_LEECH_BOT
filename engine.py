import os
import asyncio
import yt_dlp
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=3)

def _download(url, fmt):
    ydl_opts = {
        "format": fmt,
        "outtmpl": "input.mp4",
        "quiet": True,
        "noplaylist": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return "input.mp4"

async def download(url, fmt="best"):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, _download, url, fmt)

def compress_hevc(input_file, output_file="output.mp4"):
    cmd = f"""
    ffmpeg -y -i {input_file}
    -c:v libx265
    -preset veryfast
    -crf 34
    -vf "scale='min(1280,iw)':-2"
    -c:a aac -b:a 96k
    {output_file}
    """
    os.system(cmd)
    return output_file

import os
import ffmpeg
import yt_dlp
import requests
from concurrent.futures import ThreadPoolExecutor

# مخصص للعمليات الثقيلة لمنع تجميد البوت
executor = ThreadPoolExecutor(max_workers=3)

def download_video(url):
    """
    محرك تحميل ذكي:
    1. يحاول التحميل عبر yt-dlp (لليوتيوب، تيك توك، إلخ).
    2. إذا فشل، يحاول التحميل كملف مباشر (Direct Link).
    """
    output = "input.mp4"
    if os.path.exists(output): os.remove(output)
    
    # محاولة التحميل عبر yt-dlp
    try:
        ydl_opts = {
            'format': 'best',
            'outtmpl': output,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return output
    except Exception:
        # محاولة التحميل كملف مباشر إذا فشل yt-dlp
        try:
            response = requests.get(url, stream=True, timeout=10)
            with open(output, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)
            return output
        except Exception as e:
            raise Exception(f"فشل التحميل: {str(e)}")

def compress_video(input_file, resolution="720"):
    """ ضغط الفيديو بنظام HEVC مع معالجة الأخطاء """
    output_file = f"compressed_{resolution}.mp4"
    scale_map = {"360": "640:-2", "480": "854:-2", "720": "1280:-2", "1080": "1920:-2"}
    
    try:
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(
            stream, output_file, 
            vcodec='libx265', 
            crf=28, 
            vf=f"scale={scale_map.get(resolution, '1280:-2')}", 
            acodec='aac'
        )
        ffmpeg.run(stream, overwrite_output=True, capture_stdout=True, capture_stderr=True)
        return output_file
    except ffmpeg.Error as e:
        raise Exception(f"خطأ في الضغط: {e.stderr.decode()}")

def convert_to_mp3(input_file):
    """ تحويل أي ملف فيديو إلى MP3 """
    output_file = "audio.mp3"
    ffmpeg.input(input_file).output(output_file, acodec='libmp3lame', ab='128k').run(overwrite_output=True)
    return output_file

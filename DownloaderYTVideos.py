import yt_dlp
import os
from moviepy.editor import VideoFileClip
import re


def sanitize_filename(name):
    """Sanitize the filename to avoid filesystem errors."""
    return re.sub(r'[\\/*?:"<>|]', "", name)


def download_video(link, folder="assets"):
    os.makedirs(folder, exist_ok=True)
    ydl_opts = {
        'format': "best",
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(link, download=True)
        title = sanitize_filename(info.get('title', 'video'))
        video = ydl.prepare_filename(info)
        return video, title


def extract_audio(path, audio_filename, folder="assets"):
    video = VideoFileClip(path)
    audio_path = os.path.join(folder, f"{audio_filename}.mp3")
    video.audio.write_audiofile(audio_path)
    print(f"Audio extraído y guardado en: {audio_path}")


if __name__ == "__main__":
    url = input("Introduce link de video: ")
    output_folder = "assets"
    video_path, video_title = download_video(url, output_folder)
    extract_audio(video_path, video_title, output_folder)

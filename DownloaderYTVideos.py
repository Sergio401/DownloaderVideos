import yt_dlp
from moviepy.editor import VideoFileClip

def download_video(url):
    ydl_opts = {
        'format': "best",
        'outtmpl': 'video.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info_dict)
        return video_path


def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = video_path.replace('.mp4', '.mp3')
    video.audio.write_audiofile(audio_path)
    print(f"Audio extraído y guardado en: {audio_path}")


if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=NwKP92AoB04"
    video_path = download_video(url)
    extract_audio(video_path)

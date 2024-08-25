# Makefile

# Target para actualizar yt_dlp
upgrade:
	pip install --upgrade yt_dlp

download_video:
	python3 DownloaderYTVideos.py
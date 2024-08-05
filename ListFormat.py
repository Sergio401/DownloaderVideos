import yt_dlp

url = ("https://www.youtube.com/watch?v=NwKP92AoB04")

# Definir opciones para listar formatos
ydl_opts = {}

# Crear una instancia de YoutubeDL con las opciones definidas
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    formats = info_dict.get('formats', [])

    # Listar todos los formatos disponibles
    for f in formats:
        print(f'format_id: {f["format_id"]}, ext: {f["ext"]}, resolution: {f["resolution"]}, note: {f.get("note", "N/A")}')
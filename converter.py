import yt_dlp

url = "https://youtu.be/MGawAvCJUOM?si=QRFWqpWC3ivQvdiS"

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
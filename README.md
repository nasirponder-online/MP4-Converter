🎬 YouTube Video Downloader (Python + yt-dlp)

A simple and efficient Python script for downloading high-quality videos from YouTube using the powerful yt-dlp library. This project demonstrates how to fetch the best available video and audio streams and automatically merge them into a single MP4 file.

🚀 Features
Downloads videos in the best available quality
Automatically selects and merges best video + audio
Outputs a clean MP4 file
Minimal setup and easy to use
Built on top of the actively maintained yt-dlp library
🧠 How It Works

The script uses yt-dlp to:

Take a YouTube video URL as input
Fetch the highest quality video and audio streams separately
Merge them into a single .mp4 file using FFmpeg
📦 Requirements
Python 3.x
yt-dlp
FFmpeg (must be installed and available in your system PATH)

Install dependencies:

pip install yt-dlp
💻 Usage

Simply update the url variable with your desired YouTube link and run the script:

import yt_dlp

url = "https://youtu.be/MGawAvCJUOM?si=QRFWqpWC3ivQvdiS"

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
⚙️ Configuration Options

You can customize behavior by modifying ydl_opts, such as:

Choosing specific resolutions or formats
Setting output filenames
Downloading subtitles
Limiting download speed
⚠️ Disclaimer

This tool is intended for educational and personal use only. Make sure you comply with YouTube’s Terms of Service and respect copyright laws when downloading content.

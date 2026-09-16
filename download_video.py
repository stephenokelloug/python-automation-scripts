import yt_dlp
import os

# Ensure output directory exists
output_dir = os.path.join("output", "youtube")
os.makedirs(output_dir, exist_ok=True)

# Paste your YouTube video URL here
url = "https://www.youtube.com/watch?v=ZGmcC3ydDG0&list=RDZGmcC3ydDG0&start_radio=1"

# yt-dlp options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',   # highest quality
    'merge_output_format': 'mkv',           # ensure MP4 output
    'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # save with video title
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"Download complete! Saved to {output_dir}")

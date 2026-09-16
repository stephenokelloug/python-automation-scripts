import yt_dlp
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    # Choose output folder
    output_dir = filedialog.askdirectory(title="Select output folder")
    if not output_dir:
        return

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Download complete!\nSaved to {output_dir}")
    except Exception as e:
        messagebox.showerror("Download Failed", str(e))

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

tk.Button(root, text="Download Video", command=download_video).pack(pady=10)

root.mainloop()

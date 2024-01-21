import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist


def download(url, path):
    obiect = YouTube(url)
    obiect = obiect.streams.get_highest_resolution()
    obiect.download(path)


def dld_playlist(url, path):
    play = Playlist(url)
    for video in play.videos:
        video.streams.filter(
            only_audio=True).first().download(output_path=path)


def arata_calea():
    calea = filedialog.askdirectory()
    return calea


def apasa_buton():
    link = intrare.get()
    path = arata_calea()
    download(link, path)
    print("\nDownload complete!")


def apasa_playlist():
    link = new_entry.get()
    path = arata_calea()
    dld_playlist(link, path)
    print("\nDownload complete!")


window = tk.Tk()

window.geometry("500x500")
window.title("Youtube")

label = tk.Label(
    window, text="Insert the link of the VIDEO below", font=('Calibri', 16))
label.pack()

intrare = tk.Entry(window, width=70)
intrare.pack(pady=5)

buton = tk.Button(window, text="Download Video", command=apasa_buton)
buton.pack(pady=10)
label = tk.Label(window, text="Insert the link of the PLAYLIST below",
                 font=('Calibri', 16))
label.pack(pady=10)

new_entry = tk.Entry(window, width=70)
new_entry.pack(pady=5)

btn = tk.Button(window, text='Download Playlist', command=apasa_playlist)
btn.pack(pady=10)


window.mainloop()

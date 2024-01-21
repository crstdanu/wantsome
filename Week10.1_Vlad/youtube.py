from pytube import YouTube
from pytube import Playlist

youtube_url = "https://www.youtube.com/watch?v=-oPuGc05Lxs"
playlist_url = "https://www.youtube.com/playlist?list=PLiVLdIV18yeXxFi7y6b2DN4f6u2Izhl9t"

# obiect = YouTube(youtube_url)
# obiect = obiect.streams.get_highest_resolution()
# obiect.download()


play = Playlist(playlist_url)

# print(playlist) ->> asta e o lista cu ce contine playlist-ul meu

for video in play.videos:
    try:
        video.streams.filter(type="video", progressive=True).order_by(
            'resolution').desc().first().download()
    except:
        print('Eroare')
    # print(f'name: {}, url: {}'.format(video.title, video.watch_url))

from pytube import Playlist
from pytube import YouTube


def dld_playlist(url):
    play = Playlist(url)
    for video in play.videos:
        video.streams.filter(only_audio=True).first().download()
    print('Download complete!')


URL = 'https://www.youtube.com/watch?v=U6Ay9v7gK9w&list=PLiVLdIV18yeUUOs2phqMtQjjZ-bcKhsq9&index=4&t=627s&ab_channel=JasonStephenson-SleepMeditationMusic'

# dld_playlist(URL)


def dld_audio(url):
    play = YouTube(url)
    play.streams.filter(only_audio=True).first().download()
    print('Download Complete!')


URL1 = "https://www.youtube.com/watch?v=ZToicYcHIOU&list=PLiVLdIV18yeUUOs2phqMtQjjZ-bcKhsq9&index=5&t=12s&ab_channel=Calm"
URL2 = "https://www.youtube.com/watch?v=pU80BEm43JM&list=PLiVLdIV18yeUUOs2phqMtQjjZ-bcKhsq9&index=6&t=23s&ab_channel=Priory"
URL3 = "https://www.youtube.com/watch?v=syx3a1_LeFo&list=PLiVLdIV18yeUUOs2phqMtQjjZ-bcKhsq9&index=7&t=17s&ab_channel=Calm"
URL4 = "https://www.youtube.com/watch?v=xv-ejEOogaA&list=PLiVLdIV18yeUUOs2phqMtQjjZ-bcKhsq9&index=8&t=22s&ab_channel=GreatMeditation"
URL5 = "https://www.youtube.com/watch?v=uTN29kj7e-w&list=PLiVLdIV18yeUUOs2phqMtQjjZ-bcKhsq9&index=9&t=10s&ab_channel=BohoBeautifulYoga"

dld_audio(URL5)

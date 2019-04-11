from tkinter import filedialog
import tkinter as tk
import vlc
import time
def chooseFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    root.update()
    return file_path

def playMusic():
    file_path = chooseFile()
    p = vlc.MediaPlayer(file_path)

    p.play()

    while True:
        pass
def playmp3list():
    """
    p = vlc.MediaPlayer("Whatsapp.mp3")

    p.play()"""

    song_list = ["Whatsapp.mp3","michael.mp3"]
    instance = vlc.Instance()
    for song in song_list:
        player = instance.media_player_new()
        media = instance.media_new(song)
        print (song)
        media.get_mrl()
        player.set_media(media)
        player.play()
        playing = set([1, 2, 3, 4])
        time.sleep(1)  # Give time to get going
        duration = player.get_length() / 1000
        mm, ss = divmod(duration, 60)
        print ("Playing", song, "Length:", "%02d:%02d" % (mm, ss))
        while True:
            state = player.get_state()
            if state not in playing:
                break
            continue



def playwav(self):
    p = vlc.MediaPlayer("/Users/emre/bass.wav")
    p.play()

    while p.is_playing():
        pass


def main():

    print("1: Play mp3 files respectively \n")
    print("2: select mp3 \n")
    print("3: Play wav \n")

    switch = input()

    if switch == "1":
        playmp3list()
    elif switch == "2":
        playMusic()

    elif switch == "3":
        playwav()











if __name__ == '__main__':
    main()






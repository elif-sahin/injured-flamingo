

import vlc
import os
import time
import _tkinter
import tkinter as tk
from tkinter import filedialog

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

def playVideo():

    file_path = chooseFile()

    i = vlc.Instance('--verbose 2'.split())
    p = i.media_player_new()
    p.set_mrl(file_path)
    p.play()



def main():
    print("1: Play Music \n")
    print("2: Play Video \n")

    switch = input()

    if switch == "1":
        playMusic()

    if switch == "2":
        playVideo()













if __name__ == '__main__':
    main()




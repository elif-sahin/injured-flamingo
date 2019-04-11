

import vlc

class Funct:
    def playmp3(self):
        p = vlc.MediaPlayer("/Users/emre/balance.mp3")
        p.play()
        a = p.play()
        print(a)

        print(p.is_playing())


    def playwav(self):
        p = vlc.MediaPlayer("/Users/emre/bass.wav")
        p.play()

        while p.is_playing():
            pass


def main():
    print("1: Play mp3 \n")
    print("2: Play wav \n")

    switch = input()

    if switch == "1":
        Funct.playmp3(Funct)

    elif switch == "2":
        Funct.playwav(Funct)











if __name__ == '__main__':
    main()




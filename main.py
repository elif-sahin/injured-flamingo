

import simpleaudio as sa



class Audio:
    def wav(self):
        wave_obj = sa.WaveObject.from_wave_file('/Users/emre/bass.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()
    def mp3(self):
        wave_obj = sa.WaveObject.from_wave_file('/Users/emre/balance.mp3')
        play_obj = wave_obj.play()
        play_obj.wait_done()

def main():
    Audio.wav(Audio)


if __name__ == '__main__':
    main()





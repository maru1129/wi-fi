from ping3 import ping
import time
from pydub import AudioSegment
from pydub.playback import play


def sound_play(sound_file):
    sound = AudioSegment.from_file(sound_file)
    sound = sound-10    #ボリューム調整
    play(sound)


def main():
    device = "[YOUR_DEVICE_IP-ADRESS]"
    sound_file = "[YOUR_SOUNDFILE_PATH]"
    count_unconnect_time = 0

    while True:
        if ping(device):
            print("connected successfully!\nplease wait a second...")
            time.sleep(5)
            sound_play(sound_file)
            break
        else:
            print("failed to connect (_ _||||) ...")
            time.sleep(5)
            count_unconnect_time += 1

            if count_unconnect_time == 3:
                print("接続に3回失敗したので60秒後にまた確認するで")
                time.sleep(60)
                count_unconnect_time = 0


if __name__ == "__main__":
    main()





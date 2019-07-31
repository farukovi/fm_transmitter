import os
import time
import random

var = 1

while var==1:
    musicList = os.listdir('music/')
    fileCount = len(musicList)
    random.shuffle(musicList)

    i = 0
    while i < fileCount:
        if musicList[i].find('.mp3') < 0:
            continue
        
        cmd = "sox \"music/"+musicList[i]+"\" -r 22050 -c 1 -b 16 -t wav currentMusic.wav" 
        print (cmd)
        os.system(cmd)

        cmd = "sudo ./fm_transmitter/fm_transmitter -f 101.0 currentMusic.wav"
        print(cmd)
        os.system(cmd)
        time.sleep(1)
        i+=1
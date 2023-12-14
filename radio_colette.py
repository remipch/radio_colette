import os
import random
import vlc
import time
from datetime import datetime

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

path = "/home/pi/radio_colette/audio/"
all_files = os.listdir(path)

while True:
   random.shuffle(all_files)
   for random_file in all_files:
      if random_file.endswith('.mp3'):
         random_file = os.path.join(path, random_file)
         date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
         print(date_time, random_file)

         media = vlc_instance.media_new(random_file)
         player.set_media(media)
         player.play()

         while player.get_state() != vlc.State.Ended:
            time.sleep(0.1)

   print("")

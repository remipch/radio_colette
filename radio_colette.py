import os
import random
import vlc
from datetime import datetime
from gpiozero import Button
from time import sleep, time
from glob import glob

# WARNING: Keyboard and mouse are unusable while button is off

audio_glob_pattern = "/home/pi/radio_colette/audio/**/*.mp3"

# Various sleep times in seconds
sleep_between_tracks = 2
sleep_between_buttons_checks = 0.1
sleep_between_dir_list = 2 # Prevent to use all CPU if there is no MP3
wait_before_switch_usb_off = 5

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

button = Button(2)

mp3_files = []

playing_mode = None # True=ON False=OFF

off_start_time = None # Time in seconds when the off mode has been set

def startPlayNextMp3File():
   global mp3_files
   while True:
      if len(mp3_files) == 0:
         # List dir again because files may be added or removed
         mp3_files = glob(audio_glob_pattern, recursive=True)
         random.shuffle(mp3_files)

      if len(mp3_files) == 0:
         print("No MP3 found from ", audio_glob_pattern)
         sleep(sleep_between_dir_list)
      else:
         next_file = mp3_files.pop(0)
         if os.path.isfile(next_file):
            date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(date_time, next_file)
            media = vlc_instance.media_new(next_file)
            player.set_media(media)
            player.play()
            return

def stopPlaying():
   player.stop()

def isPlayerPlaying():
   return player.get_state() != vlc.State.Ended

def isButtonPressed():
   return button.is_pressed

def switchUsbOn():
   os.system("sudo uhubctl -l 1-1 -p 2 -a 1 > /tmp/uhubctl.log")

def switchUsbOff():
   os.system("sudo uhubctl -l 1-1 -p 2 -a 0 > /tmp/uhubctl.log")

def setMode(mode):
   global playing_mode, off_start_time
   playing_mode = mode
   if mode:
      startPlayNextMp3File()
   else:
      print("OFF: Waiting button press\n")
      stopPlaying()
      off_start_time = time()

switchUsbOn()
setMode(isButtonPressed())

while True:
   if playing_mode:
      if isButtonPressed():
         if isPlayerPlaying():
            sleep(sleep_between_buttons_checks)
         else:
            sleep(sleep_between_tracks)
            setMode(True)
      else:
         setMode(False)
   else:
      sleep(sleep_between_buttons_checks)
      if isButtonPressed():
         switchUsbOn()
         setMode(True)
      elif off_start_time is not None and (time() - off_start_time) > wait_before_switch_usb_off:
         off_start_time = None
         switchUsbOff()

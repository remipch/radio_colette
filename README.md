# Radio Colette :notes:

Minimalist MP3 player for Mamie Colette, my grandmother :older_woman: :two_hearts:

By "minimalist", I mean the whole user interface is :

![A single button](button.jpg)

A single button allows to switch between 2 modes :
- On : indefinitely play all MP3 files randomly
- Off : stop playing

Behind the button is a Raspberry Pi 3 B with external speakers powered by USB.

Volume control is on external speakers.

Button state is read by Raspberry Pi GPIO2 input.

USB power is switched off when the button is off.

| :warning: It makes keyboard and mouse unusable while button is off |
|--------------------------------------------------------------------|

## Install

### Install Raspberry Pi SD card

Using rpi-installer, choose `RASPBERRY PI OS (LEGACY)` with desktop and
security updates, without recommanded applications.

Insert SD card and start the Pi.

### Install python-vlc

A usefull lib to play audio files from python.

```
pip install python-vlc
```

### Install uhubctl

A usefull tool to switch USB power ON/OFF programmatically.

```
sudo apt-get install libusb-1.0-0-dev
cd ~
git clone https://github.com/mvp/uhubctl
cd uhubctl
make
sudo make install
```

### Install radio_colette

```
cd ~
git clone https://github.com/remipch/radio_colette
```

### Manual config

Copy some MP3 files to `/home/pi/radio_colette/audio/` directory.

Enable audio output from "Device Profiles" icon :
- Disable HDMI Digital Stereo Output
- Enable AV Jack Analog Stereo Output

Autostart radio_colette (from
[forums.raspberrypi.com](https://forums.raspberrypi.com/viewtopic.php?t=294014)) :

```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```

and add this line at the end :

`@lxterminal -e python3 /home/pi/radio_colette/radio_colette.py`

### Electrical setup

GPIO2 has a builtin pullup, just connect the button between GPIO2 and GND, so :
- On = connected circuit = play
- Off = disconnected circuit = stop

From [raspberry.com](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html),
here is the GPIO pinout :

![GPIO pinout](pinout.png)

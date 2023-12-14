# Radio Colette

Minimalist MP3 player for Mamie Colette.

By "minimalist", I mean the whole user interface is :

![A single button](button.jpg)

A single button allows to switch between 2 modes :
- On : indefinitely play all MP3 files randomly
- Off : stop playing

Behind the button is a Raspberry Pi 3 B with external speakers powered by USB.

Volume control is on external speakers.

Button state is read by Raspberry Pi GPIO.

USB power is switched off when the button is off.

## Install

### Install Raspberry Pi SD card

Using rpi-installer, choose `RASPBERRY PI OS (LEGACY)` with security updates, without recommanded applications.

Insert SD card and reboot the Pi.

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


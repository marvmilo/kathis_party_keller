# LED install
```
git clone https://github.com/jgarff/rpi_ws281x
cd rpi_ws281x/
git checkout ee7522e3b053950af33bc7e4364742cd3aeaf594
sudo scons
cd python
sudo python3 setup.py build
sudo python3 setup.py install
sudo pip3 install adafruit-circuitpython-neopixel
```
# Modes Static
## Single Color (single):
- color
## Two Color blured (two_color):
- color1
- color2
- blur factor → 0px - 150px
# Modes Animation
## Pulse (pulse):
- color1
- color2
- interval → 1s - 10s
## Shoot (shoot):
- color1
- color 2
- interval → 1s - 10s
- fade out → 5s - 20s
- blur factor → 0px - 10px
## Rainbow (rainbow):
- interval → 10s - 100s
# Modes Audio Visiulizer
## Pegel (audio_pegel):
- color1
- color2
- fade out → 0s - 10s
- blur factor → 0px - 50px
## Shoot (audio_shoot):
- color1
- color2
- fade out → 5s - 20s
- blur factor → 0px - 10px
## Brightness (audio_brightness):
- color1
- color2
- fade out → 0s - 10s
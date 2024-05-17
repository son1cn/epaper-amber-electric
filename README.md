# epaper-amber-electric
![PXL_20240517_101023159](https://github.com/son1cn/epaper-amber-electric/assets/31121758/ef97df76-9359-41b7-a097-82985ac3465e)

I had an old raspberry pi and epaper display from an old project [epaper-crypto-ticker](https://github.com/son1cn/epaper-crypto-ticker) lying around and thought to get it working again, but this time to monitor real time electricity price that I am paying to be more conscious during the day.

Just like last time:
[PapiRus with 2.7in E-Ink Display](https://au.rs-online.com/web/p/raspberry-pi-screens/1218357/)

Start with a fresh [Raspbian Buster Lite image](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip) (or whatever version is available now) with [SSH enabled](https://phoenixnap.com/kb/enable-ssh-raspberry-pi), set up a static IP (easiest from the DHCP server side) to make it easier to remote in later at a known address.

Pull this repo somewhere easy, I used the home directory.

Using the install instructions linked on the store page [PapiRus on GitHub](https://github.com/PiSupply/PaPiRus) to install the drivers on the pi.
After following the automated install, **ensuring you select Python 2 and 3 when prompted**
>#### Auto Installation
>Just run the following script in a terminal window and PaPiRus will be automatically setup.
>```bash
># Run this line and PaPiRus will be setup and installed
>curl -sSL https://pisupp.ly/papiruscode | sudo bash
>```
#### Install python3 pip
```bash
sudo apt-get install python3-pip
```
#### Install [amberelectric](https://pypi.org/project/amberelectric)
```bash
pip3 install amberelectric
```

#### Update the checkamber.py file with your API key

#### Make display.py executable
You need to make display.py executable (needs to be done anytime a git pull is performed on this repo)
```bash
chmod +x display.py
```

install the script to run every minute via cron
```bash
crontab -e
```
add the following to the bottom, with the path to your display.py
```bash
* * * * * /home/pi/epaper-amber-electric/display.py
```

### Enjoy!

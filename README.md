# VMC Project
## A Simple integration project for HeltyAir VMC through irda interface

The project is based on the following hw/sw components:
- Raspberry Pi Zero W (https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
- ANAVI Infrared pHAT (https://anavi.technology/)
- Zero Stem Usb interface (https://zerostem.io/)
- Lircd
- Python3

This is the first poc:
![poc](/images/vmc.jpeg)

## Features

- Multiroom support
- Send commands via http GET method (ex: curl "http://YOUR_IP/room=studio&cmd=up")

## Installation

Pre-requirements:

- [Raspberry] - The Raspian system is installed
- [ANAVI Infrared pHAT] - It's configured in the right way (please refer to to official documentation - https://github.com/AnaviTechnology/anavi-docs/blob/master/anavi-infrared-phat/anavi-infrared-phat.md -)
- [Zero Stem Usb interface] - It's installed and recognized by Raspian OS (please refer to to official documentation - https://zerostem.io/)
- [Lircd] - It is installed (please refer to the ANAVI official documentation - https://github.com/AnaviTechnology/anavi-docs/blob/master/anavi-infrared-phat/anavi-infrared-phat.md -) 

A brief description of the installation steps:
```sh
sudo apt install -y python3-pip
git clone https://github.com/ftorn/vmc.git
cd vmc
sudo pip3 install -r requirements.txt
sudo mv vmc.conf /etc/lirc/lircd.conf.d
sudo systemctl restart lircd
sudo cp vmc.service /lib/systemd/
sudo mv api.py /home/pi/
sudo systemctl enable vmc
```
If you want to change the room name or the cmd names edit these two files:

- api.py 
- vmc.conf [lircd configuration file]

Edit the 'api.py' file and change these two lines:
```sh
rooms = ['vmc']
cmds = ['off', 'powerfull', 'up', 'down', 'cooling', 'light']
```
Edit the 'vmc.conf' file and change these lines:
```sh
name   vmc (begin remote section)
name   COMMANDS (begin raw_codes)
```


If you want to expose a different tcp port (I use the default http port - 80) you could execute the api.py in this way (please you have to change the vmc.service file or you have to edit the api.py code):
```sh
sudo ./api.py 8080
```
## Test

Open a shell and execute:
```sh
curl "http://YOUR_IP/room=studio&cmd=up"
```

## ToDo

- Modbus integration
- Create a case (3d model for 3d printer)


# EMFFAX 2022

EMFFAX is appearing in both bars at [EMF 2022](https://emfcamp.org). This repo contains the
code used to generate its pages.

A snapshot of the tti files created by this repo can be found at
https://github.com/mscroggs/emffax-2022-tti.

## Setting up EMFFAX

### Hardware

Get a Raspberry Pi Zero and solder wires onto the TV and GND
connectors. Note that on a Pi Zero 2 (and maybe other Pis), the connectors
are to the left of the labels, not the right.

Attach the other ends of these wires to a phono connector (GND is -, TV is +).

### Software

Install Raspberry Pi OS Lite on a micro SD card, and boot up the Pi.

Edit the file `/boot/cpnfig.txt` and comment out the line `dtoverlay=vc4-kms-v3d`.

#### vbit2

Install [vbit2](https://github.com/peterkvt80/vbit2). This can be done by running:

```bash
source <(wget -O - https://raw.githubusercontent.com/peterkvt80/vbit2/master/getvbit2)
```

Once vbit2 has installed, it will launch the vbit2 config tool. First,
select `Install service` > `Custom` > `git repo` and enter
`https://github.com/mscroggs/emffax-2022-tti`, enter the name `EMFFAX`,
then set this as the main service.

Next, go into options, and set vbit2 to run at boot (option can be toggled
using the spacebar).

Finally, start vbit2 then exit the config tool.

#### EMFFAX

Clone this repo, using:

```bash
git clone https://github.com/mscroggs/emffax-2022.git
```

Make a copy of `localconfig.py.template` called `localconfig.py`, and add the line
`output_dir = "/home/USERNAME/.teletext_services/EMFFAX"`. You can also add any
local settings you wish to use (eg API keys).

#### Cron jobs

Add the following cron jobs:

```
@reboot cd /home/USERNAME/EMFFAX && python stream_subtitles.py
*/10 * * * * cd /home/USERNAME/EMFFAX && python build_pages.py
```

Add the following to the .bashrc file:

```
if $(ps aux | grep "screensaver.py" | grep -v "grep" > /dev/null); then
    echo "screensaver already running."
else
  python /home/USERNAME/EMFFAX/screensaver.py
fi
```

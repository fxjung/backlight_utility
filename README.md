# Backlight Utility

Screen brightness control utility for at least Thinkpad T490


- Free software: MIT license
- Documentation: https://backlight-utility.readthedocs.io.


Features
--------

### Installation

```bash
git clone git@github.com:fxjung/backlight_utility.git
cd backlight_utility
pip install -e .[dev]
pre-commit install
```

### Setup

Create `.env` file containing the paths to the respective files:
```dotenv
BRIGHTNESS_PATH=/sys/class/backlight/intel_backlight/brightness
MAX_BRIGHTNESS_PATH=/sys/class/backlight/intel_backlight/max_brightness
ACTUAL_BRIGHTNESS_PATH=/sys/class/backlight/intel_backlight/actual_brightness
```

Keep in mind that these files need to be writable by the user running this software. 
This can e.g. be achieved by means of a udev rule (`/etc/udev/rules.d/99-backlight.rules`):

```udev
ACTION=="add", SUBSYSTEM=="backlight", RUN+="/bin/chgrp video /sys/class/backlight/intel_backlight/brightness", RUN+="/bin/chmod g+w /sys/class/backlight/intel_backlight/brightness" 
```

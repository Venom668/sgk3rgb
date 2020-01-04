# Sharkoon Skiller Mech SGK3 tool for controlling RGB lightning

## Requirements

```
PyQt5 (tested with 5.13.0)
pyusb (tested with 1.0.2)
```

## Installation
```
git clone https://github.com/Venom668/sgk3rgb.git 
cd sgk3rgb
pip install -r requirements.txt
```

## Usage
This program needs permissions to detach keyboard from kernel.

### With GUI:

Start with `sudo python -m sgk3rgb`

Select color and click with mouse on button you want to change.

### without GUI (in that case you don't need PyQt5):

`sudo python sgk3rgb/core/ctl.py --help`
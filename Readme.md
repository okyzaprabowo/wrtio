# Python OpenWRT GPIO

This is simple shell scripting and Python library for accessing GPIO OpenWRT
Tested in GL.Inet Router

At first, upload all of files in this repo to your router, and then copy pinmode, readpin, and write to /bin folder. 

### You can use "pinmode" like:
> use: pinmode config_method pin_number
> example: pinmode output 21

### You can use "readpin" like:
> use: readpin pin_number
> example: readpin 21

### You can use "writepin" like:
> use: use: writepin value pin_number
> example: writepin 1 21

Post about my code:
https://okyzaprabowo.wordpress.com/2015/08/29/simple-shell-scripting-for-accessing-openwrt-router-gpio/

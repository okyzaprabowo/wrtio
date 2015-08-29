This is simple shell scripting for accessing GPIO OpenWRT
Tested in GL.Inet Router

You can use "pinmode" like:
use: pinmode config_method pin_number
example: pinmode output 21

You can use "readpin" like:
use: readpin pin_number
example: readpin 21

You can use "writepin" like:
use: use: writepin value pin_number
example: writepin 1 21
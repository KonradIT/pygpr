# PyGPR

Dead simple GoPro GPR RAW format wrapper for Python

[More info on .GPR files](https://github.com/gopro/gpr)

## Up and running:

    git clone https://github.com/konradit/pygpr
    cd pygpr
    sudo python3 setup.py install
    

## Usage:


    >>> from pygpr import gpr
    >>> gpr_obj = gpr()
    >>> gpr_obj.convert("GOPR0001.GPR,"Raw_sunset.DNG")

    # __init__() constructor needs path to gpr_tools!
    
## Examples:


1. Converts all *.GPR raw files in my SD card to DNG to edit easier later (I use Luminance to apply presets and then export to JPG)

    from os import listdir
    from os.path import isfile, join
    from pygpr import gpr

    gpr_obj = gpr()

    raw_images = [f for f in listdir(".") if isfile(join(".", f)) and f.endswith(".GPR")]
    for img in raw_images:
        dng_name=img.split(".GPR")[0]+".DNG"
        gpr_obj.convert(img, dng_name)

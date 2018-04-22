from os import listdir
from os.path import isfile, join
from pygpr import gpr
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-x", "--gpr", help = "path to the gpr program")

args = vars(ap.parse_args())
gpr_obj = gpr(args["gpr"])

raw_images = [f for f in listdir(".") if isfile(join(".", f)) and f.endswith(".GPR")]
for img in raw_images:
	dng_name=img.split(".GPR")[0]+".DNG"
	gpr_obj.convert(img, dng_name)

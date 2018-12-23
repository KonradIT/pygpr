import argparse
from pygpr import gpr

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-o", "--out", help = "path to the output file")
ap.add_argument("-x", "--gpr", help = "path to the gpr program", default="gpr_tools")

args = vars(ap.parse_args())

print("Converting",args["image"])

gpr_obj = gpr(args["gpr"])
gpr_obj.convert(args["image"],args["out"])

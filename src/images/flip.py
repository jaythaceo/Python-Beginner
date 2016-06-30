from PIL import Image
import os

filelist = 'polar.jpeg'

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpeg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot covert", infile

import sys
import math
import kfasta
from array import array
try:
    from PIL import Image
except ImportError:
    print "You don't have PIL (the python Imaging Library) installed.  Try..."
    print "  - on Debian/Ubuntu/etc., apt-get install python-imaging"
    print "  - on MacOS X with MacPorts, port install py27-pil"
    print "  - on Windows, the hell with you I Googled for 30 minutes, track down a binary from somewhere."
    sys.exit(-1)

# A simple 2D integer  array immplementation on top of Pythons built in imaging library.
class Array2D:
    def __init__(self, typecode, w, h, defaultval):
        self.arr = array(typecode, [defaultval]*(w*h))
        self.w = w
        self.h = h
    def put(self, x, y, v):
        """docstring for put"""
        assert x >= 0 and x < self.w
        assert y >= 0 and y < self.h
        self.arr[(y*self.w)+x] = v
    def incr(self, x, y)):
        """docstring for incr"""
        assert x >= 0 and x < self.w
        assert y >= 0 and y < self.h
        self.arr[(y*self.w)+x] += 1
    def get(self, x, y):
        assert x >= 0 and x < self.w
        assert y >= 0 and y < self.h
        return self.arr[(y*self.w)+x]
    def max(self):
        return max(self.arr)

### High-level driver code. No need to tweak this EVER. ###

# Given a sequence of matches, produces a w-by-h image and saves it to filename.
# The remapping function takes values in (0,1) and returns values in (0,1); the default
# value (fourth-root) makes lightly-populated bins considerably darker.
def buildComparisonImage(filename, w, h, alen, blen, matches, remapfn=lambda x:math.sqrt(math.sqrt(x))):
    """docstring for buildComparisonImage"""
    arr = Array2D('L', w, h, 0L)
    print "Sequence A length: " + str(alen)
    print "Sequence B length: " + str(blen)
    abinsize = int(math.ceil(alen / float(w)))
    bbinsize = int(math.ceil(blen / float(h)))
    assert abinsize > 0 and bbinsize > 0
    print "Binnning matches..."
    for m in matches:
        #print m (abinsize, bbinsize), (m[0]//abinsize, m[1]//bbinsize), (w, h)
        arr.incr(m[0] // abinsize, m[1] // bbinsize)
        print "...done binning matches."
        print "Normalizing and plotting results..."
        maxval = float(arr.max())
        img = Image.new('RGB', (w,h))
        for y in range(0, h):
            for x in range(0, w):
                val = 255 - int(math.ceil(remapfn((arr.get(x,y) / maxval)) * 255.0))
                img.putpixel((x,y), (val, val, val))
        print "...done normalizing and plotting."
        img.save(filename)

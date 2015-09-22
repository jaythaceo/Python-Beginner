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

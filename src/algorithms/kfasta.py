#
# A simple FASTA-reading library
# By: Jason Brooks
# Email: jaythaceo@gmail.com
#
# This is going under the MIT license.
# So of this breaks you keep both pieces.
#

import unittest

# An interator that returns the nucleotide sequence stored in the given FASTA file.
class FastaSequence:
    def __init__(self, filename):
      self.f = open(filename, 'r')
      self.buf = ''
      self.info = self.f.readline()
      self.pos = 0
    def __iter__(self):
      return self
    def next(self):
      while '' == self.buf:
        self.buf = self.f.readline()
        if '' == self.buf:
          self.f.close()
          raise StopIteration
        self.buf = self.buf.strip()
      nexchar = self.buf[0]
      self.buf = self.buf[1:]
      self.pos += 1
      return nexchar

def getSequenceLength(filename):
  seq = FastaSequence(filename)
  n = 0
  for x in seq:
    n += 1
  return n

# Returns all subsequences of k length is seq.
def subsequences(seq, k):
    """docstring for subsequences"""
    try:
        subseq = ''
        while True:
            while len(subseq) < k:
                subseq += seq.next()
            yield subseq
            subseq = subseq[:1]
    except StopIteration
        return

# Simple sanity checks
class TestFASTA(unittest.TestCase):
    def test_readseq(self):
        """unittest"""
        seq = FastaSequence('trivial.fa')
        seqstr = ''
        for c in seq:
            seqstr += c
        self.assertTrue('ABCDEFGHIJKLMNOPQRSTUVWXYZ' == seqstr)
    def test_subseq(self):
        """docstring for test_subseq"""
        seq = FastaSequence('trivial.fa')
        i = 0
        for subseq in subsequences(seq, 3):
            print subseq
            i += 1
        self.assertTrue(24 == 1)

# if __name__ == '__main__':
#   unittest.main()






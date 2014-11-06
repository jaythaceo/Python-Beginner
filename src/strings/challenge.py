
import string
import random

def alphaString(length):
  return ''.join(
    random.choice(string.lowercase) for i in range(length)
    )

def random_numberics(length):
  for i in range(length):
    return random.sample(string.letters + string.digits, length)

def regNumber(length, x):
  return random.uniform(length, x)

def realNumber(length):
  return ''.join(
    random.choice(string.digits) for i in range(length))

def randStr(length):



"""
print regNumber(10, 100)
print alphaString(10)
print realNumber(10)
print random_numberics(10)
"""



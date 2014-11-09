
import string
import random

length = 10

def alphaString(length):
  return ''.join(
    random.choice(string.lowercase) for i in range(length)
    )

def random_numberics(length):
  i  = length
  for i in range(length):
    return random.choice(string.letters + string.digits)

def regNumber(length, x):
  return random.uniform(length, x)

def realNumber(length):
  return ''.join(
    random.choice(string.digits) for i in range(length))


print alphaString(10)
print regNumber(10, 100)
print alphaString(10)
print random_numberics(10)

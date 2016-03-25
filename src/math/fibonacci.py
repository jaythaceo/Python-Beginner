
import math
import sys

# crazy shit
def fib_rek(n):
  if n == 0:
    return 0

  if n == 1:
    return 1

  else:
    return fib_rek(n-1) + fib_rek(n-2)

# dynamic programming
def fib_mem(n):
  m = []
  for i in range(n+1):
    m.append(-1)

  m[0] = 0
  m[1] = 1
  def fib_mem_rek(n):
    if m[n] != -1:
      return m[n]
    else:
      val = fib_mem_rek(n-1) + fib_mem_rek(n-2)
      m[n] = val
      return val
  return fib_mem_rek(n)

# moivre-binet formula "yes I know shit like this"
def fib_close(n):
  return int((1.0 / math.sqrt(5)) * (math.pow(((1.0 + math.sqrt(5)) / 2), n) - math.pow(((1.0 - math.sqrt(5)) / 2), n)))
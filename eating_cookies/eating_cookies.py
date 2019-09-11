#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

counter = 0

def count(n, counter):
  pass

def eating_cookies(n, cache=None):
  counter = 0
  # good solution - should increment possibilities by 1
  if cache[n] != 0:
    return cache[n]
  
  else:
    cookies_to_eat = [1, 2, 3]
    for num in cookies_to_eat:
      if n == 0:
        return 1
      elif n - num < 0:
        break
      else:
        counter += eating_cookies(n - num, cache)
  
  cache[n] = counter
  return counter

cache = [0] * 101

print(eating_cookies(50, cache))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
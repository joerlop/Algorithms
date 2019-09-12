#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  possibilities = ["rock", "paper", "scissors"]

  possible_plays = []

  if n == 0:
    return [[]]

  elif n == 1:
    return [["rock"], ["paper"], ["scissors"]]

  else:
    possible_plays = rock_paper_scissors(n-1)
    print(f"possible plays: {possible_plays}")
    
    result = []

    for item in possible_plays:
      print(f"item: {item}")

      for i in range(3):
        new_item = item + [possibilities[i]]
        print(f"new item: {new_item}")
        print(f"item: {item}")
        print(f"item to include: {new_item}")
        result.append(new_item)

  return result

print(rock_paper_scissors(3))



"""
0
---
[]

1
---
[[0], [1], [2]]

loop through the result of n-1 and append element in list to each 0, 1, 2

2
---
[[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]


3
---
[
  [0,0,0], [0,0,1], [0,0,2]
  [0,1,0], [0,1,1], [0,1,2]

"""


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
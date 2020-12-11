#!/usr/bin/env python

import requests
import sys

expenses_url = "https://adventofcode.com/2020/day/3/input"
cookies = {"session": "53616c7465645f5ffd3fe2aefcf4895beb9941ea79e8730bc182b86e1e27ce09fb53b7043984472a39efcd20a43fdbea"}

puzzle_input = list(filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n")))



def generate_geology(traverse_right, traverse_down, puzzle_input):
  geology = list()
  height = len(puzzle_input)
  width = len(puzzle_input[0])
  
  # Total width needed
  total_width_multiplier = int((traverse_right * height) / width)
  if ((traverse_right* height) % width) > 0:
    total_width_multiplier += 1
  
  for line in puzzle_input:
    geology.append(list(line) * total_width_multiplier)

  return geology

def check_slope(traverse_right, traverse_down, geology):
  row_index = 0
  col_index = 0
  num_trees = 0
  num_empty = 0

  while row_index < len(geology):
    col_index += traverse_right
    row_index += traverse_down

    if (row_index) < len(geology):
      if geology[row_index][col_index] == "#":
        num_trees += 1
      else:
        num_empty += 1

  print("NUMBER OF TREES: {}".format(num_trees))
  return num_trees

slopes = [
  {"right": 3, "down": 1}, # Part 1
  {"right": 1, "down": 1},
  {"right": 5, "down": 1},
  {"right": 7, "down": 1},
  {"right": 1, "down": 2},
]

total_trees_encountered = 1

for slope in slopes:
  right = slope['right']
  down = slope['down']

  geo = generate_geology(right, down, puzzle_input)
  
  total_trees_encountered *= check_slope(right, down, geo)

print("TOTAL TREES MULTIPLIED: {}".format(total_trees_encountered))



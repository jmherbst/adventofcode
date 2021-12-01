#!/usr/bin/env python

import requests
import sys

expenses_url = "https://adventofcode.com/2020/day/1/input"
cookies = {"session": "53616c7465645f5ffd3fe2aefcf4895beb9941ea79e8730bc182b86e1e27ce09fb53b7043984472a39efcd20a43fdbea"}


expenses = list(map(int, filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n"))))

# PART 1
for num in expenses:
  diff = 2020 - num
  if diff in expenses:
    print("PART 1:   Numbers are: {} and {}.  Total multiplied: {}".format(num, diff, num * diff))
    break

# PART 2
for first_num in expenses:
  first_diff = 2020 - first_num
  for second_num in expenses:
    second_diff = first_diff - second_num
    if second_diff in expenses:
      print("PART 2:   Numbers are: {} and {} and {}.  Total multiplied: {}".format(first_num, second_num, second_diff, first_num * second_num * second_diff))
      sys.exit(0)


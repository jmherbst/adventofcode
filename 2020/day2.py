#!/usr/bin/env python

import requests
import sys

expenses_url = "https://adventofcode.com/2020/day/2/input"
cookies = {"session": "53616c7465645f5ffd3fe2aefcf4895beb9941ea79e8730bc182b86e1e27ce09fb53b7043984472a39efcd20a43fdbea"}

passwords = list(filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n")))

valid = 0
invalid = 0

# PART 1
for row in passwords:
  rule, password = row.split(':', 1)
  occ, char = rule.split(' ', 1)
  low, high = occ.split('-', 1)


  if password.count(char) < int(low) or password.count(char) > int(high):
    invalid += 1
  else:
    valid += 1

print("Total valid: {} --- Total invalid: {}".format(valid, invalid))


# PART 2
valid = 0
invalid = 0

for row in passwords:
  rule, password = row.split(':', 1)
  password = password.strip()
  occ, char = rule.split(' ', 1)
  low, high = map(int, occ.split('-', 1))


  if password[low-1] == char and not password[high-1] == char:
    valid += 1
    print("LOW MATCH:  password: '{}',  char: {},  {}(low)-{}(high)".format(password, char, low, high))
  elif password[high-1] == char and not password[low-1] == char:
    valid += 1
    print("HIGH MATCH:  password: '{}',  char: {},  {}(low)-{}(high)".format(password, char, low, high))
  else:
    invalid += 1
    print("INVALID:  password: '{}',  char: {},  {}(low)-{}(high)".format(password, char, low, high))

print("Total valid: {} --- Total invalid: {}".format(valid, invalid))


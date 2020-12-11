#!/usr/bin/env python

import requests
import math

expenses_url = "https://adventofcode.com/2020/day/5/input"
cookies = {"session": "53616c7465645f5ffd3fe2aefcf4895beb9941ea79e8730bc182b86e1e27ce09fb53b7043984472a39efcd20a43fdbea"}

puzzle_input = list(filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n")))

highest_seat_id = 0 
SEATING_CHART = [ [None] * 8 for i in range(128) ]


def find_next(bmin, bmax, direction):
  # THIS CAN"T WORK FOR BOTH LEFT AND RIGHT. Look into which to use floor vs ceil
  if direction == "down":
    return bmin + math.floor((bmax - bmin) / 2)
  if direction == "up":
    return bmin + math.ceil((bmax - bmin) / 2)

def find_row(row_code):
  min_row = 0
  max_row = 127

  #print("START ROW: {} - {}".format(min_row, max_row))

  for val in row_code:
    if val == "F":
      max_row = find_next(min_row, max_row, "down")
      #print("F: {} - {}".format(min_row, max_row))
    elif val == "B":
      min_row = find_next(min_row, max_row, "up")
      #print("B: {} - {}".format(min_row, max_row))
  
  return min_row 

def find_col(col_code):
  min_col = 0
  max_col = 7

  #print("START COL: {} - {}".format(min_col, max_col))

  for val in col_code:
    if val == "L":
      max_col = find_next(min_col, max_col, "down")
      #print("L: {} - {}".format(min_col, max_col))
    elif val == "R":
      min_col = find_next(min_col, max_col, "up")
      #print("R: {} - {}".format(min_col, max_col))
  
  return min_col 

seat_ids = []

for seat in puzzle_input:
  # separate the code into rows+columns
  row_code = seat[:-3] # F or B
  col_code = seat[-3:] # R or L

  row_num = find_row(row_code)
  col_num = find_col(col_code)

  seat_id = (row_num * 8) + col_num
  seat_ids.append(seat_id)
  if seat_id > highest_seat_id:
    highest_seat_id = seat_id

seat_ids.sort()

for i in range(len(seat_ids)):
  if i == 0:
    continue
  elif seat_ids[i] == seat_ids[len(seat_ids)-1]:
    print("we're at the end....")
  else:
    if (seat_ids[i] + 1) != seat_ids[i+1]:
      your_seat_id = seat_ids[i] + 1
    if (seat_ids[i] - 1) != seat_ids[i-1]:
      your_seat_id = seat_ids[i] - 1

print("HIGHEST SEAT ID: {}".format(highest_seat_id))
print("YOUR SEAT ID: {}".format(your_seat_id))


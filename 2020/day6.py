#!/usr/bin/env python

import os
import requests

from dotenv import load_dotenv

load_dotenv()

expenses_url = "https://adventofcode.com/2020/day/6/input"
cookies = {"session": os.getenv("SESSION_ID")}

puzzle_input = list(filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n\n")))

def remove_dupes(s):
  deduped = ""
  for i in s:
    if i in deduped:
      pass
    else:
      deduped = deduped + i

  return deduped

def get_dupes(group_answers):
  dupe_holder = None

  if len(group_answers) == 1:
    return group_answers[0]
  else:
    for answers in group_answers:
      if dupe_holder is None:
        dupe_holder = list(answers)
      else:
        dupes = "".join(set(dupe_holder) & set(answers))
        if dupes == "":
          return list()
        else:
          dupe_holder = list(dupes)
      
  return dupe_holder


# ------ Part 1 -------
total_yes = 0

for group in puzzle_input:
  deduped_group = remove_dupes(group.replace("\n", ""))
  
  for number in deduped_group:
    total_yes += len(number)

print("PART 1 --- TOTAL YES's: {}".format(total_yes))
     

# ------ Part 2 -------
part2_total_yes = 0

for group in puzzle_input:
  group = list(filter(None, group.split("\n")))
  dupes = get_dupes(group)
  part2_total_yes += len(dupes)

print("PART 2 --- TOTAL YES's: {}".format(part2_total_yes))

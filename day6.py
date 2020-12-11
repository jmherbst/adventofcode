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

def count_dupes(group_answers):
  print(group_answers)
  dupe_holder = list()

  if len(group_answers) == 1:
    print("ONLY A SINGLE PERSON {}".format(group_answers))
    return len(group_answers[0])
  else:
    for answers in group_answers:
      if len(dupe_holder) == 0:
        dupe_holder = sorted(list(answers))
        print("First try. Dupeholder is empty. New holder = {}".format(dupe_holder))
      else:
        print("Dupeholder: {} ----- Next group: {}".format(''.join(dupe_holder), ''.join(sorted(answers))))
        dupe_holder = ''.join(set(dupe_holder) & set(sorted(answers)))
        print(list(dupe_holder))
      
  return len(dupe_holder)


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
  part2_total_yes += count_dupes(group)
  print("TOTAL: {}".format(part2_total_yes))


print("PART 2 --- TOTAL YES's: {}".format(part2_total_yes))

#!/usr/bin/env python


import os
import requests

from dotenv import load_dotenv

load_dotenv()

expenses_url = "https://adventofcode.com/2020/day/7/input"
cookies = {"session": os.getenv("SESSION_ID")}

puzzle_input = list(filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n")))

def get_number_of_bags(description):
  return int(description.split(" ")[0])

def get_color_of_bag(description):
   return " ".join(description.split(" ")[1:3]).replace(".", "")

def buid_inverse_bag_dict(rules):
  bags = {}

  while len(rules) > 0:
    print("LENGTH: {}".format(len(rules)))
    # First iteration gets bags with nothing in them
    # Subsequent iterations add to empty bag dicts with names containing empty bags
    for rule in rules:
      bag_color = rule.split("bags ")[0].strip()

      # the remainder of the rule string after "contain" is all the internal bag colors and quantities
      contains = rule.split("contain ")[1]
      contains_list = contains.split(",")

      if contains == "no other bags.":
        bags[bag_color] = {}
        rules.remove(rule)
        print(bags)
      else:
        for bag in contains_list:
          bag_details = bag.strip()
          contains_qty = get_number_of_bags(bag_details)
          contains_color = get_color_of_bag(bag_details).strip()
          print("BAGS: {}\nColor:{}".format(bags,contains_color))
          if contains_color in bags:
            bags[contains_color] = {contains_color: contains_qty}
            print(contains_list)
            contains_list.remove(bag)
            print(contains_list)
          else:
            continue
  print(bags)

def build_bag_dict(rules):
  bags = {}
  for rule in puzzle_input:
    bag_color = rule.split("bags")[0]
    bags[bag_color] = {} 
    bag = bags[bag_color]
    
    # the remainder of the rule string after "contain" is all the internal bag colors and quantities
    contains = rule.split("contain ")[1]
    if contains == "no other bags.":
      ### DO SOMETHING HERE FOR 0
      continue
  
    contains_list = contains.split(",")
  
    # there is only 1 type of bag within this color
    if len(contains_list) == 1:
      contains_qty = get_number_of_bags(contains_list[0])
      contains_color = get_color_of_bag(contains_list[0])
      if contains_color not in bag:
        bag[contains_color] = contains_qty
  
    else: # there is more than 1 internal bag
      for bag_details in contains_list:
        bag_details = bag_details.strip()
        contains_qty = get_number_of_bags(bag_details)
        contains_color = get_color_of_bag(bag_details)
        if contains_color not in bag:
          bag[contains_color] = contains_qty
         
  return bags


# Part 1
BAG_COLOR = "shiny gold"
contains_count = 0

bags = buid_inverse_bag_dict(puzzle_input)
for bag, contents in bags.items():
  print("{} --- {}".format(bag, contents))
  if BAG_COLOR in contents:
    contains_count += 1

print(contains_count)

#!/usr/bin/env python

import requests
import re

expenses_url = "https://adventofcode.com/2020/day/4/input"
cookies = {"session": "53616c7465645f5ffd3fe2aefcf4895beb9941ea79e8730bc182b86e1e27ce09fb53b7043984472a39efcd20a43fdbea"}

puzzle_input = requests.get(expenses_url, cookies=cookies).text.split("\n\n")


total_valid = 0

cid_regex = re.compile(r'.*cid:(\d+).*')

def has_required_fields(passport):
  required_field_regexes = {
    "byr": re.compile(r'.*byr:(\d{4}).*'),
    "iyr": re.compile(r'.*iyr:(\d{4}).*'),
    "eyr": re.compile(r'.*eyr:(\d{4}).*'),
    "hgt": re.compile(r'.*hgt:([0-9]+cm|[0-9]+in).*'),
    #"hcl": re.compile(r'.*hcl:(#[0-9a-zA-Z){6}.*'),
    "ecl": re.compile(r'.*ecl:(.*)\s{1}.*'),
    "pid": re.compile(r'.*pid:(.*)\s{1}.*'),
  }
  part_two_required_field_regexes = [
    re.compile(r'.*byr:(19[2-9][0-9]|200[0-2]).*'),
    re.compile(r'.*iyr:(201[0-9]|2020).*'),
    re.compile(r'.*eyr:(202[0-9]|2030).*'),
    re.compile(r'.*hgt:(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in).*'),
    re.compile(r'.*hcl:(#[0-9a-f]{6}).*'),
    re.compile(r'.*ecl:(amb|blu|brn|gry|grn|hzl|oth).*'),
    re.compile(r'.*pid:([0-9]{9}).*'),
  ]
  part_one_required_field_regexes = [
    re.compile(r'.*(byr:).*'),
    re.compile(r'.*(iyr:).*'),
    re.compile(r'.*(eyr:).*'),
    re.compile(r'.*(hgt:).*'),
    re.compile(r'.*(hcl:).*'),
    re.compile(r'.*(ecl:).*'),
    re.compile(r'.*(pid:).*'),
  ]

  #for field, regex in required_field_regexes.items():
  #  if field == "byr":
  #    match = regex.findall(passport) 
  #    if len(match) == 0:
  #      return False
  #    else:
  #      match = match[0]
  #      if len(match) == 4 and 1920 <= int(match) <= 2002:
  #        #print("VALID: *{}* inside of range 1920-2002".format(match))
  #        continue
  #      else:
  #        #print("*{}* is outside of range 1920-2002".format(match))
  #        return False
  #  if field == "iyr":
  #    match = regex.findall(passport) 
  #    if len(match) == 0:
  #      return False
  #    else:
  #      match = match[0]
  #      if len(match) == 4 and 2010 <= int(match) <= 2020:
  #        #print("VALID: *{}* inside of range 2010-2020".format(match))
  #        continue
  #      else:
  #        #print("*{}* is outside of range 2010-2020".format(match))
  #        return False
  #  if field == "eyr":
  #    match = regex.findall(passport) 
  #    if len(match) == 0:
  #      return False
  #    else:
  #      match = match[0]
  #      if len(match) == 4 and 2020 <= int(match) <= 2030:
  #        #print("VALID: *{}* inside of range 2020-2030".format(match))
  #        continue
  #      else:
  #        #print("*{}* is outside of range 2020-2030".format(match))
  #        return False
  #  if field == "hgt":
  #    match = regex.findall(passport) 
  #    if len(match) == 0:
  #      return False
  #    else:
  #      match = match[0]
  #      num = int(match[:-2])
  #      unit = match[-2:]
  #      if (unit == "cm" and 150 <= num <= 193) or (unit == "in" and 59 <= num <= 76):
  #        print("VALID: *{}* inside of range 150-193cm or 59-76in".format(match))
  #        continue
  #      else:
  #        print("*{}* is outside of range 150-193cm or 59-76in".format(match))
  #        return False
  #  if field == "hcl":
  #    match = regex.findall(passport) 
  #    if len(match) == 0:
  #      return False
  #    else:
  #      match = match[0]
  #      if match[0] == "#" and not re.search("[g-z]", match):
  #        print("VALID: *{}* ".format(match))
  #        continue
  #      else:
  #        print("*{}* Not a valid color code".format(match))
  #        return False
  #  # case "ecl":
  #  # case "pid":
      
  for regex in part_two_required_field_regexes:
    matches = regex.findall(passport)
    if regex == re.compile(r'.*hcl:(#[0-9a-f]{6}).*'):
      print(matches)
    if len(matches) == 0:
      return False

  return True

for passport in puzzle_input:
  passport = passport.replace("\n", " ")
  if has_required_fields(passport):
    total_valid += 1 

print("TOTAL VALID: {}".format(total_valid))



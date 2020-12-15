#!/usr/bin/env python

import os
import requests

from dotenv import load_dotenv

load_dotenv()

expenses_url = "https://adventofcode.com/2020/day/7/input"
cookies = {"session": os.getenv("SESSION_ID")}

puzzle_input = list(filter(None, requests.get(expenses_url, cookies=cookies).text.split("\n\n")))


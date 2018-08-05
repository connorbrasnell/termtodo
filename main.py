#!/usr/bin/env python3
"""
The main file used for the termtodo project.
"""

import argparse
import json

# Standard output file
output_file = "json_data/todolist.json"

# Counter variable
counter = 0

# Set up the argument parser
parser = argparse.ArgumentParser(description='Command line arguments.')
parser.add_argument('-a', dest='to_add', help='Add a todo item.')
OPTIONS = parser.parse_args()

# Initalise to_do_list, used if the json file is empty
to_do_list = {}

# Read from the json file, and set to_do_list to the items if the file is not empty
read_from = open(output_file, 'r')
lines = read_from.read()
if lines:
    to_do_list = json.loads(lines)
read_from.close()

# Figure out what ID the new item needs to be
while str(counter) in to_do_list and to_do_list:
    counter = counter + 1

if OPTIONS.to_add:
    to_do_list[counter] = [OPTIONS.to_add]

write_to = open(output_file, 'w')
write_to.write(json.dumps(to_do_list))
write_to.close()

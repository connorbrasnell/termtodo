#!/usr/bin/env python3
"""
The main file used for the termtodo project.
"""

import argparse
import json

# Standard output file
output_file = "json_data/todolist.json"

# Set up the argument parser
parser = argparse.ArgumentParser(description='Command line arguments.')
parser.add_argument('-o', dest='output', action='store_true', help='Output the to do list.')
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

def add_item(item):
    # Counter variable
    counter = 0

    # Figure out what ID the new item needs to be
    while str(counter) in to_do_list and to_do_list:
        counter = counter + 1

    to_do_list[counter] = [item]

    write_to = open(output_file, 'w')
    write_to.write(json.dumps(to_do_list))
    write_to.close()

def display_items():
    for item in to_do_list:
        print(str(item) + '\t' + str(to_do_list[item][0]))

if OPTIONS.to_add:
    add_item(OPTIONS.to_add)
if OPTIONS.output:
    display_items()

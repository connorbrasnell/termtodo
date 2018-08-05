#!/usr/bin/env python3
"""
The main file used for the termtodo project.
"""

import argparse

parser = argparse.ArgumentParser(description='Command line arguments.')
parser.add_argument('-a', dest='to_add', help='Add a todo item.')
OPTIONS = parser.parse_args()

to_do_list = []

if OPTIONS.to_add:
    to_do_list.append(OPTIONS.to_add)

for item in to_do_list:
    print(item)
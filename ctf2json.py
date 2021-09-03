#!/usr/bin/env python

import json
from argparse import ArgumentParser
from ctf_parser import convert_line, convert_file, save_json_to_file

parser = ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)

group.add_argument("-f", "--file", required=False,
                   dest="filename", type=str,
                   help="Input CTF file to be converted to Json")
group.add_argument("-l", "--line", required=False,
                   dest="line", type=str,
                   help="Input CTF line to be converted to Json")
args = parser.parse_args()

if args.line:
    json_obj = convert_line(args.line)
    print(json.dumps(json_obj, indent=4, sort_keys=True))

if args.filename:
    output_json_filename = args.filename + ".json"
    json_obj = convert_file(args.filename)
    save_json_to_file(json_obj, output_json_filename)

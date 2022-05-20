import json
from mapper import exist_rules, get_rules, is_sales_draft, rules
import re
from line_converter import *
import sys


def parse_line(str, lens):
    result = {}
    position = 0
    for len in lens:
        result[len[1]] = str[position:position+len[0]]
        position += len[0]
    return result


def get_tc(line):
    return line[0:2]


def get_tcr(line):
    tcr = line[3]
    # print(tcr)
    if is_sales_draft(get_tc(line)) and tcr == "2":
        # print(tcr + line[16:18])
        return tcr + line[16:18]
    else:
        return tcr


def convert_line(line):
    if is_bundle(line):
        line = convert_bundle(line)
    if is_itf(line):
        line = convert_itf_to_ctf(line)
    if not is_ctf(line):
        sys.exit("Unknown file type, aborting.")
    tc = get_tc(line)
    tcr = get_tcr(line)
    if exist_rules(tc, tcr):
        return parse_line(line, get_rules(tc, tcr))


def convert_file(filename):
    ctf_filename = filename

    ctf = []
    parsedLines = []
    with open(ctf_filename, 'r') as reader:
        ctf = reader.readlines()
    for ctfLine in ctf:
        parsedLine = convert_line(ctfLine)
        if parsedLine:
            parsedLines.append(parsedLine)
    return parsedLines


def save_json_to_file(json_obj, filename):
    with open(filename, 'w') as writer:
        writer.write(json.dumps(json_obj, indent=4, sort_keys=True))

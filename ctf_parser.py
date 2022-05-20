from mapper import *
from line_converter import *


def parse_line(str, lens):
    result = {}
    position = 0
    for len in lens:
        result[len[1]] = str[position:position+len[0]]
        position += len[0]
    return result


def get_tc(line):
    if is_tc_of_type(line[0:2], "multipurpose"):
        return line[0:2] + line[16:19]
    else:
        return line[0:2]


def get_tcr(line):
    tcr = line[3]
    if tcr == "2" and (is_tc_of_type(get_tc(line), "sales draft") or is_tc_of_type(get_tc(line), "fee collection")):
        return tcr + line[16:18]
    else:
        return tcr


def convert_line_to_ctf(line):
    if is_bundle(line):
        line = convert_bundle(line)
    if is_itf(line):
        line = convert_itf_to_ctf(line)
    if is_ctf(line):
        return line
    else:
        return ""


def process_line(line):
    line = convert_line_to_ctf(line)
    if line:
        tc = get_tc(line)
        tcr = get_tcr(line)
        if exist_rules(tc, tcr):
            return parse_line(line, get_rules(tc, tcr))
        else:
            print("no rule for TC " + tc + " TCR " + tcr)
    else:
        return ""


def convert_file(filename):
    ctf_filename = filename

    ctf = []
    parsedLines = []
    with open(ctf_filename, 'r') as reader:
        ctf = reader.readlines()
    for ctfLine in ctf:
        parsedLine = process_line(ctfLine)
        if parsedLine:
            parsedLines.append(parsedLine)
    return parsedLines

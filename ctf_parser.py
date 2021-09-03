import json
from mapper import exist_rules, get_rules, rules


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
    return line[3]


def convert_line(line):
    tc = get_tc(line)
    tcr = get_tcr(line)
    if exist_rules(tc, tcr):
        return parse_line(line, get_rules(tc, tcr))


def convert_file(filename):
    ctf_filename = filename
    json_filename = ctf_filename+".json"

    ctf = []
    parsedLines = []
    with open(ctf_filename, 'r') as reader:
        ctf = reader.readlines()
    for ctfLine in ctf:
        parsedLine = convert_line(ctfLine)
        parsedLines.append(parsedLine)
    return parsedLines


def save_json_to_file(json_obj, filename):
    with open(filename, 'w') as writer:
        writer.write(json.dumps(json_obj, indent=4, sort_keys=True))

import re

CTF_LINE_LENGTH = 170
ITF_LINE_LENGTH = 172


def is_itf(line):
    return len(line) == ITF_LINE_LENGTH


def is_ctf(line):
    return len(line) == CTF_LINE_LENGTH


def is_bundle(line):
    pattern = re.compile("^key:.*Data:")
    return pattern.match(line)


def convert_itf_to_ctf(line):
    outputLine = line[0:2] + line[4:]
    return outputLine


def convert_bundle(line):
    outputLine = re.sub('^key:.*Data:', '', line)
    return outputLine

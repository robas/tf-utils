#!/usr/bin/env python

from argparse import ArgumentParser
from ctf_parser import convert_file, get_file_types
from tc_parser import *
import csv

parser = ArgumentParser()
arg_group = parser.add_argument_group()

arg_group.add_argument("-f", "--file", required=True,
                       dest="filename", type=str,
                       help="Input CTF/ITF/Bundle file to be processed")

arg_group.add_argument("-tc", "--transactioncode", required=True,
                       dest="tc", type=str,
                       help="Target transaction code (TC) to filter for")

arg_group.add_argument("-fields", "--fields", required=True,
                       dest="fields", type=str,
                       help="Fields name to filter")

args = parser.parse_args()

if args.filename:
    tcs = []
    fields = []
    resultSet = []
    output_csv_filename = args.filename + ".csv"

    inputFileTypes = get_file_types(args.filename)
    print("Input file types detected: " + inputFileTypes)

    tcs = convert_file(args.filename)

    if args.tc:
        filteredTCs = filterTC(tcs, args.tc)

    if args.fields:
        fields = [f.strip() for f in args.fields.split(",")]
        for tc in filteredTCs:
            resultSet.append(getTCFields(tc, fields))
        with open(output_csv_filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            for a in resultSet:
                writer.writerow(a)
    print("Generated {}, with {} rows".format(
        output_csv_filename, len(resultSet)))

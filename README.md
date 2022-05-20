# TF Utils

> Misc tools to help with CTF, ITF and Bundle files.

## Intro

Ctfxtract script allows the extraction of specific fields from specific TCs in CTF/ITF/Bundle files.

TF Tools currently supports:

- Parsing of CTF, ITF and Bundle files
- Extraction of CLI specified fields to a .csv file

## Usage

```shell
usage: ctfxtract.py [-h] -f FILENAME -tc TC -fields FIELDS

optional arguments:
  -h, --help            show this help message and exit

  -f FILENAME, --file FILENAME
                        Input CTF/ITF/Bundle file to be processed
  -tc TC, --transactioncode TC
                        Target transaction code (TC) to filter for
  -fields FIELDS, --fields FIELDS
                        Fields name to filter
```

Note: In order to be able to directly execute the file with `./ctfxtract.py` instead of `python ctfxtract.py`, it is necessary to allow the file execution with:

```shell
chmod +x ctfxtract.py
```

### Examples

```shell
./ctfxtract.py -f "FILENAME.ITF" -tc 05 -fields "Acquirer Reference Number,Merchant Category Code,Merchant City,Source Amount,Source Currency Code"
```

```shell
./ctfxtract.py -f files/TEST.ITF -tc 20 -fields "Transaction Identifier, Source Amount,Reason Code, Country Code,Event Date (MMDD),Message Text"
```
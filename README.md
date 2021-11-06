# TF Utils

> Misc tools to help with CTF and ITF files.

## Intro

TF Tools currently supports the convertion of Sales Draft TCR0 and TCR1 transactions to JSON.

## Usage

Ctf2json script allows conversion of files and lines.
Before directly executing the script, it is necessary to allow the file execution with:

```shell
chmod +x ctf2json
```

### File

```shell
./ctf2json -f "filename.ctf"
or
python ctf2json -f "filename.ctf"
```

### Line

```shell
./ctf2json -l "0501            000000 PSIRF            MEMBER FREE TEXT AND GOES 2 HERE.       888888888888888        000000000000  0000001P  5 0  -ITEM DESCRIPTOR FOR 25--000000000  "

```

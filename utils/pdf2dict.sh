#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit 1
fi

FILE=$1
DICTFILE=$FILE.dict

if [ ! -f $FILE ]
then
    echo "The provided argument must be a file."
    exit 1
fi
cp $FILE $DICTFILE

sed -i '' -E 's/^[0-9]+ //' $DICTFILE
sed -i '' -E 's/^[0-9]+\–[0-9]+ //' $DICTFILE
sed -i '' -E 's/^[0-9]+\-[0-9]+ //' $DICTFILE
sed -i '' -E 's/( UN| AN| ANS| DX| N)//' $DICTFILE
sed -i '' -E "s/^([0-9]+) (.*)/[\1, '\2'],/" $DICTFILE
sed -i '' -E '$s/,$//' $DICTFILE
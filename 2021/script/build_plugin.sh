#!/bin/bash
# build_plugin.sh builds one go plugin, given a day

BASEDIR=$(dirname "$0")

# If the number of arguments is not 1, then print usage instructions and exit
if [[ $# -ne 1 ]]; then
    echo "Usage: ./build_plugin.sh <day>"
    exit 1
fi

YEAR=2021
DAY=$1

# If DAY is not an integer between 1 and 31, print error and exit
if ! [[ $DAY =~ ^[012]?[0-9]$ ]] && ! [[ $DAY =~ ^3[01]$ ]]; then
    echo "Invalid <day>. Must be between 1 and 31, inclusive."
    exit 1
fi

# If DAY is one digit, left-pad with a zero
if [[ $DAY =~ ^[0-9]$ ]]; then
    DAY="0$DAY"
fi

DIR="$BASEDIR/../$DAY"

# If DIR exists, cd into it and run build script
if [[ -d $DIR ]]; then
    cd $DIR
    go build -buildmode=plugin -o $YEAR$DAY.so
else
    echo "$DIR does not exist"
    exit 1
fi

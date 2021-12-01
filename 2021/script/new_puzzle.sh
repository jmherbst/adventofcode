#/bin/bash
# new_puzzle.sh creates a new folder and copies template files for a new day's puzzle

BASEDIR=$(dirname "$0")
source $BASEDIR/../.env

# If the number of arguments is not 1, then print usage instructions and exit
if [[ $# -ne 1 ]]; then
    echo "Usage: ./new_puzzle.sh <day>"
    exit 1
fi

DAY=$1
YEAR=2021

# If DAY is not an integer between 1 and 31, print error and exit
if ! [[ $DAY =~ ^[12]?[0-9]$ ]] && ! [[ $DAY =~ ^3[01]$ ]]; then
    echo "Invalid <day>. Must be between 1 and 31, inclusive."
    exit 1
fi

# Create header for new README
README="# [$YEAR Day $DAY:](https://adventofcode.com/$YEAR/day/$DAY)\n\n## Original Brief\n\n"

# If DAY is one digit, left-pad with a zero
if [[ $DAY =~ ^[0-9]$ ]]; then
    PADDED_DAY="0$DAY"
fi

DIR="$BASEDIR/../$PADDED_DAY"

if [[ -d $DIR ]]; then
    echo "Error: Directory \"$DIR already exists.\""
    exit 1
fi

mkdir -p $DIR

# Copy template files (or variable string) into the new puzzle files
cp $BASEDIR/../main.go.templ $DIR/main.go
echo $README > $DIR/README.md

# Get puzzle input and put into input.txt file
curl -s -X GET https://adventofcode.com/$YEAR/day/$DAY/input -H "Cookie: session=$SESSION_ID" > $DIR/input.txt

# DunCash
Script so that the Duncan Treasurers don't have to manually create DunCash word clouds.

## Requirements
This script runs on Python 2, and requires the [wordcloud Python package](https://github.com/amueller/word_cloud). Also of note, this package requires NumPy.

## Use
To run, invoke this script with your Python interpreter and provide two arguments:
infile, the csv which contains expense categories and dollar amounts separated by a newline.
outfile, the file to write the image to.

Invocation for some infile expenses.csv and outfile image.png would look like:

`python DunCash.py /path/to/expenses.csv /path/to/image.png`

import argparse
import csv
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud

__author__ = 'github.com/samshadwell'


def green_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(120, 76%%, %d%%)" % random.randint(0, 60)


def main():
    """
    Main function. Give the program the file of CSV to generate a word cloud from.
    :return: None.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="The csv to generate a DunCash graphic from")
    parser.add_argument("outfile", help="The file to write the resulting word cloud to")
    args = parser.parse_args()

    with open(args.infile) as csvfile:
        reader = csv.reader(csvfile)
        word_totals = []
        for row in reader:
            out_word = row[0].strip() + " - " + row[1].strip()
            out_freq = float(row[1][row[1].index('$') + 1:])
            word_totals.append((out_word, out_freq))

        wc = WordCloud(height=300, width=1000, background_color="white", color_func=green_color_func)
        wc.fit_words(word_totals)
        #wc.to_file(args.outfile)

        plt.imshow(wc)
        plt.axis("off")
        plt.show()


if __name__ == "__main__":
    main()

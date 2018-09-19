import string
from collections import defaultdict
import argparse
import logging


"""
Here is the file I used to get the bigrams. I like how what you did is simple. I broke mine into different methods 
because that's what I like to do and it can be easier to follow sometimes when it is broken up. But that is just 
personal preference.
"""


def read_file(filename):
    """
    Reads and returns segmented text
    :param filename: str
    :return: list
    """
    logging.info('Reading %s' % filename)
    punctuation = set(string.punctuation)
    with open(filename, 'r', encoding='utf-8') as f:
        segmented_text = []
        for l in f.readlines():
            text_lower = l.strip().lower()
            text_cleaned = ''.join([c for c in text_lower if c not in punctuation])
            text_split = text_cleaned.split()
            segmented_text.extend(text_split)
        return segmented_text


def get_bigrams(segmented_text):
    """
    Returns bigram tuples from presegmented text
    :param segmented_text: list
    :return: list
    """
    logging.info('Getting bigrams')
    return [bg for bg in zip(segmented_text[:-1], segmented_text[1:])]


def get_bg_counts(bigrams):
    """
    Counts bigrams
    :param bigrams: list
    :return: dict
    """
    logging.info('Getting bigram counts')
    bigram_counts = defaultdict(int)
    for bg in bigrams:
        if bg in bigram_counts.keys():
            bigram_counts[bg] += 1
        else:
            bigram_counts[bg] = 1
    return bigram_counts


def bg_to_tsv(bg_dict, filename):
    """
    Writes list of bigrams to file
    :param bg_dict: dict
    :param filename: str
    """
    logging.info('Writing to TSV')
    sorted_keys = sorted(bg_dict, key=bg_dict.get, reverse=True)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('bigram\tcount')
        for k in sorted_keys:
            f.write('\n%s\t%s' % (k, bg_dict[k]))
        f.close()
    logging.info('Successfully written to TSV')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    parser = argparse.ArgumentParser(description='Takes a .txt file and writes all bigrams excluding punctuation to a '
                                                 'TSV file.')
    parser.add_argument('text', metavar='TEXT_FILE', nargs=1)
    parser.add_argument('tsv', metavar='TSV_FILE', nargs=1)

    txt_file = parser.parse_args().text[0]
    tsv_file = parser.parse_args().tsv[0]

    input_text = read_file(txt_file)
    bigrams = get_bigrams(input_text)
    bigrams_dict = get_bg_counts(bigrams)
    bg_to_tsv(bigrams_dict, tsv_file)

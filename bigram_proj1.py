import string
import operator


def make_bigrams_count(infile):  # Python varnames should be with '_' or camel case if that is what evyones using
    """
    This method makes bigrams with a bigrams count from a .txt documen
    :param infile: str
    :return: dict() sorted_bigrams_count
    """
    bigrams = []
    prev_word = ''
    bigrams_count = dict()
    exclude = set(string.punctuation)
    with open(infile) as f:
        for i in f.read().lower().split():
            word = ''.join(ch for ch in i if ch not in exclude)  # See, you did list comprehension here!
            bigrams.append(prev_word + ' ' + word)
            prev_word = word
        for bigram in bigrams:
            if bigram not in bigrams_count:
                bigrams_count[bigram] = 1
            else:
                bigrams_count[bigram] += 1
        sorted_bigram_count = sorted(bigrams_count.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_bigram_count


def put_bigrams_to_file(filename, outputfile):
    """
    This method makes bigrams with a bigrams count from a .txt document
    it also prints the results line by line to an output file of your choosing
    :param filename: str
    :param outputfile: str
    """
    sortedbigramcount = make_bigrams_count(filename)
    with open(outputfile, 'w') as f:
        for n in sortedbigramcount:
            f.write('%s:%s\n' % n)


if __name__ == '__main__':
    # these I just use to test it
    # print(makebigramscount('communist_manifesto.txt'))
    put_bigrams_to_file('communist_manifesto.txt', 'bigram_communist_manifesto.txt')

import string
import operator

#this method makes bigrams with a bigrams count from a .txt documen
#returns sortedbigramscount dict ()
def makebigramscount(infile):
    bigrams = []
    prev_word = ''
    bigram = ''
    bigramscount = dict()
    exclude = set(string.punctuation)
    with open(infile) as f:
        for i in f.read().lower().split():
            word = ''.join(ch for ch in i if ch not in exclude)
            bigrams.append(prev_word + ' ' + word)
            prev_word = word
        for bigram in bigrams:
            if bigram not in bigramscount:
                bigramscount[bigram] = 1
            else:
                bigramscount[bigram] += 1
        sortedbigramcount = sorted(bigramscount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedbigramcount

#this method makes bigrams with a bigrams count from a .txt document
#it also prints the results line by line to an output file of your choosing
def putbigramstofile(filename, outputfile):
    sortedbigramcount = makebigramscount(filename)
    with open(outputfile, 'w') as f:
        for n in sortedbigramcount:
            f.write('%s:%s\n' % n)

#print(makebigramscount('communist_manifesto.txt'))
putbigramstofile('communist_manifesto.txt', 'bigram_communist_manifesto.txt')

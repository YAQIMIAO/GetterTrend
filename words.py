import random

class words:
    BEGINNING_OF_SENTENCE = 0
    END_OF_SENTENCE = 1

    def __init__(self, caseSensitive=False):
        """
        words object constructor: creates an empty dictionary with
        case-sensitive to be false by default.
        """
        self._caseSensitive = caseSensitive
        self._words = dict()

    def add_subsequent_word(self, prev, next):
        """
        prev: a previous word
        next: a following word
        increase the count of next in the dictionary for words following
        prev
        """
        if not self._caseSensitive:
            if type(prev) is str:
                prev = prev.lower()
            if type(next) is str:
                next = next.lower()

        if next not in self._words[prev]:
            self._words[prev][next] = 0
        self._words[prev][next] += 1

    def add_sentence(self, sentence):
        """
        sentence: a string of text
        parse the sentence into a list of word and put each word in
        the dictionary for the previous word's following word.
        """
        tokens = sentence.split()
        if not self._caseSensitive:
            tokens = [word.lower() for word in tokens]

        add_subsequent_word(BEGINNING_OF_SENTENCE, tokens[0])
        for i in xrange(len(tokens) - 1):
            add_subsequent_word(tokens[i], tokens[i+1])
        add_subsequent_word(tokens[-1], END_OF_SENTENCE)

    def gen_next(self, prev):
        """
        prev: a word
        Given a word, generate random subsequent word by probability.
        """
        if not self._caseSensitive:
            if type(prev) is str:
                prev = prev.lower()

        sample_index = int( random.random() * sum(self._words[prev].values()))
        for next_word in self._words[prev]:
            if self._words[prev][next_word] < sample_index:
                sample_index -= self._words[prev][next_word]
            else:
                return next_word

    def gen_sentence(self, maxlength):
        """
        maxlength: the limit of the length of the returned sentence in chars
        Generate sentence of within a given length.
        """
        s = ''
        start = BEGINNING_OF_SENTENCE
        next_word += gen_next(start)
        while len(s) +len(next_word) <=maxlength:
            s += next_word
            if next_word != END_OF_SENTENCE:
                next_word = gen_next(next_word)
            else:
                break
        return s

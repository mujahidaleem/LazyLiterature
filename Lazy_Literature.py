from typing import List, Dict, Tuple, TextIO

import random


def associate_pair(d: Dict[Tuple[str], List[str]], key: str, value: str):
    '''Add the key-value pair to d. keys may need to be associated with
    multiple values, so values are placed in a list.
    Assumption: key is immutable
    '''
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]


def random_element(lst: List[object]) -> object:
    '''Return a random element of nonempty lst.
    '''

    return lst[random.randint(0, len(lst) - 1)]


def make_dictionary(f: TextIO, context_length: int) -> Dict[Tuple[str], List[str]]:
    '''Return a dictionary where the keys are tuples of length context_length
    containing words in f and the value for a key is the list of words
    that were found to follow the key in f.
    '''

    d = {}
    context = ('',) * context_length

    for line in f:
        word_list = line.split()
        for word in word_list:
            associate_pair(d, context, word)
            context = context[1:] + (word,)
    return d





def train_dictionary(filename: str, d: Dict[Tuple[str], List[str]], context_length: int):
    f = open(filename)
    context = ('',) * context_length
    for line in f:
        word_list = line.split()
        for word in word_list:
            associate_pair(d, context, word)
            context = context[1:] + (word,)
    f.close()


def mimic_text(word_dict: Dict[Tuple[str], List[str]], num_words: int,
               context_length: int) -> str:
    '''Based on the word patterns in word_dict, return a string that mimics
    that text, and has num_words words. context_length is the length of the
    tuples in word_dict.
    '''

    story = ''
    context = random_element(list(d.keys()))

    for i in range(num_words):

        if context in d:
            word = random_element(word_dict[context])
        else:
            context = random_element(list(d.keys()))
            word = random_element(word_dict[context])

        story = story + ' ' + word # add to story
        context = context[1:] + (word,)

    return story

"""

if __name__ == '__main__':
    # Read a text and remember the words and what comes after them in a dict
    f = open(input("Training text: ")) #Import a piece of literature here
    d = make_dictionary(f)
    f.close()
    print(mimic_text(d, 100))

    if context not in d: 
            context = random_element(list(word_dict.keys()))
"""






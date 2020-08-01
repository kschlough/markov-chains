"""Generate Markov text from text files."""

from random import choice
from collections import defaultdict


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    return text_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    for i in range(len(words)-2):
        pair = (words[i], words[i+1])
        value = words[i+2]
        if pair in chains:
            word_list = chains[pair]
            word_list.append(value)
        else:
            chains[pair] = [] 
            chains[pair].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    list_chains = list(chains.keys())    
    random_tuple = choice(list_chains)


    if random_tuple in chains:
        third_word = choice(chains[random_tuple])

        words.append(random_tuple[0])
        words.append(random_tuple[1])
        words.append(third_word)
    
    # this is our loop
    while True:
    # this is vaguely gross, too many type changes
        new_key = tuple(words[-2:])

        if new_key in chains:
            last_word = choice(chains[new_key])
            words.append(last_word)
        else:
            break


    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

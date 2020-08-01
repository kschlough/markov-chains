"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    text_string = file.read()
    file.close()

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

    # set a stopping point 
    words.append(None)

    for i in range(len(words) - 2):
        pair = (words[i], words[i + 1])
        value = words[i + 2]
        if pair not in chains:
            chains[pair] = [] 

        chains[pair].append(value)

    return chains


def make_text(chains):
    """Return text from chains."""
   
    random_tuple = choice(list(chains.keys()))
    words = [random_tuple[0], random_tuple[1]]
    third_word = choice(chains[random_tuple])
    words.append(third_word)
    
    while third_word is not None:
        random_tuple = (random_tuple[1], third_word)
        words.append(third_word)
        third_word = choice(chains[random_tuple])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

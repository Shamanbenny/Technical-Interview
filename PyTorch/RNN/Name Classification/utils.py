"""
This utility Python file is also a part of the PyTorch RNN model for name classification.
References: https://www.youtube.com/watch?v=WEV61GmmPrk&list=PLqnslRFeH2UrcDBWF5mfPGpqQDSta6VK4&index=19
"""
import string
import unicodedata
import glob

import torch

# Contains small and capital letters, space, period, comma, semicolon, and apostrophe
POSSIBLE_LETTERS = string.ascii_letters + " .,;'"
N_LETTERS = len(POSSIBLE_LETTERS)

# Converts a Unicode String to plain ASCII within the range of POSSIBLE_LETTERS, thanks to https://stackoverflow.com/a/518232/2809427
def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn'
        and c in POSSIBLE_LETTERS
    )

def load_data():
    category_lines = {}
    all_categories = []

    def find_files(path): return glob.glob(path)

    # Read a file and split into lines
    def read_lines(filename):
        lines = open(filename, encoding='utf-8').read().strip().split('\n')
        return [unicode_to_ascii(line) for line in lines]
    
    for filename in find_files('data/names/*.txt'):
        # Extract category from filename
        category = filename.split('/')[-1].split('.')[0]

        all_categories.append(category)

        # Read lines from file
        lines = read_lines(filename)
        category_lines[category] = lines

    return category_lines, all_categories

# Uses One-Hot Encoding to convert a letter to a <1 x n_letters> tensor
def letter_to_tensor(letter):
    tensor = torch.zeros(1, N_LETTERS)
    letter_index = POSSIBLE_LETTERS.find(letter)
    tensor[0][letter_index] = 1
    return tensor

def line_to_tensor(line):
    tensor = torch.zeros(len(line), 1, N_LETTERS)
    for l_idx, letter in enumerate(line):
        letter_index = POSSIBLE_LETTERS.find(letter)
        tensor[l_idx][0][letter_index] = 1
    return tensor

if __name__ == '__main__':
    print(POSSIBLE_LETTERS)
    print(unicode_to_ascii('Ślusàrski'))
    
    category_lines, all_categories = load_data()
    print(category_lines['Italian'][:5])
    
    print(letter_to_tensor('J')) # [1, 57]
    print(line_to_tensor('Jones').size()) # [5, 1, 57]
#!/usr/bin/env python3
"""Replace letters to create new word"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Replace letters to create new word',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('substring',
                        metavar='str',
                        help='Substring to replace')

    parser.add_argument('word', metavar='str', help='Word')

    parser.add_argument('-w',
                        '--wordlist',
                        help='File of words',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='/usr/share/dict/words')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sub = args.substring
    word = args.word

    if sub not in word:
        sys.exit(f'Substring "{sub}" does not appear in word "{word}"')

    pattern = word.replace(sub, '[a-z]{' + str(len(sub)) + '}')
    regex = re.compile('^' + pattern + '$')

    def match(check):
        return check != word and regex.match(check)

    if words := list(filter(match, args.wordlist.read().split())):
        print('\n'.join(words))
    else:
        print('Womp womp')


# --------------------------------------------------
if __name__ == '__main__':
    main()

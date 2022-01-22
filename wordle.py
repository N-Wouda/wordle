import os
import sys
from argparse import ArgumentParser
from pathlib import Path

from classes import Dictionary, Wordle


def usage() -> str:
    return R"""wordle.py <known> <hints> [<guesses>] [--dict=<dict>]

    <known> is a string of letters that are known to be in the word.
        Examples:
            "*****" - all letters are unknown
            "*E***" - the letter E is known to be in the second position
    <hints> is a string of letters that are known to be in the word,
        but are not necessarily in the correct position.
        Examples:
            "*"   - no known hints
            "NTE" - the letters N, T, and E are known to be in the word
            "EE"  - the letter E is known to be in the word twice
    <guesses> are earlier attempts at guessing the word.
    <dict> is the dictionary file to use. Defaults to English.
    """


def parse_args():
    parser = ArgumentParser(description="Wordle", usage=usage())
    parser.add_argument('known')
    parser.add_argument('hints', default='*', help='hints')
    parser.add_argument('guesses', default=[], nargs='*', help='guesses')
    parser.add_argument('--dict', default='en', help='dictionary')

    return parser.parse_args()


def main():
    path = Path(sys.argv[0])
    os.chdir(path.parent.resolve())

    args = parse_args()

    known = args.known.lower()
    hints = args.hints.lower()
    guesses = [guess.lower() for guess in args.guesses]

    wordle = Wordle(guesses, hints, known)

    for word in Dictionary(f"dicts/{args.dict.lower()}.txt"):
        if wordle.match(word):
            print(word.upper())


if __name__ == "__main__":
    main()

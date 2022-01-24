import os
import sys
from argparse import ArgumentParser
from glob import iglob
from pathlib import Path

from src.classes import Dictionary, Wordle


def usage() -> str:
    return R"""wordle.py <known> [<guesses>] [--hints=<hints>] [--dict=<dict>]

    <known> is a string of letters that are known to be in the word. Examples:
            "*****" - all letters are unknown
            "*E***" - the letter E is known to be in the second position
    <guesses> are earlier attempts at guessing the word.
    <hints> is a string of letters that are known to be in the word,
        but are not necessarily in the correct position. Examples:
            "*"   - no known hints
            "NTE" - the letters N, T, and E are known to be in the word
            "EE"  - the letter E is known to be in the word twice
    <dict> is the dictionary file to use. Defaults to English.
    """


def parse_args():
    parser = ArgumentParser(description="Wordle", usage=usage())

    parser.add_argument('known')
    parser.add_argument('guesses', default=[], nargs='*')
    parser.add_argument('--hints', default='*')

    dicts = [Path(path).stem for path in iglob('dicts/??.txt')]
    parser.add_argument('--dict', default='en', choices=dicts)

    return parser.parse_args()


def main():
    path = Path(sys.argv[0])
    os.chdir(path.parent.resolve())

    args = parse_args()
    wordle = Wordle(args.guesses, args.hints, args.known)

    for word in Dictionary(f"dicts/{args.dict.lower()}.txt"):
        if wordle.match(word):
            print(word.upper())


if __name__ == "__main__":
    main()

from collections import Counter
from dataclasses import dataclass


@dataclass
class Wordle:
    guesses: list[str]
    hints: str
    correct: str

    def __post_init__(self):
        self.guesses = [guess.upper() for guess in self.guesses]
        self.hints = self.hints.upper()
        self.correct = self.correct.upper()

    @property
    def not_in_word(self) -> set[str]:
        correct = set(self.correct)
        hints = set(self.hints)

        return {char
                for word in self.guesses
                for char in word
                if char not in correct and char not in hints}

    def match(self, guess: str) -> bool:
        assert guess.isalpha()
        guess = guess.upper()

        hint_count = Counter(self.hints)
        known_count = Counter(self.correct)
        guess_count = Counter(guess)

        remainder = guess_count - known_count

        def length_ok():
            return len(guess) == 5

        def letters_can_be_in_word():
            # Only letters we have not already ruled out.
            return all(c not in self.not_in_word for c in guess)

        def correct_letters_respected():
            return all(c == '*' or c == g for c, g in zip(self.correct, guess))

        def hints_ok():
            # The letters in the hint are all in the word.
            return all(remainder[c] >= cnt for c, cnt in hint_count.items()
                       if c != '*')

        def hint_positions_ok():
            # Hinted letter is in the word, but not in this position,
            # since we already tried that in a previous guess.
            return not any(p != c and p == g and p in hint_count
                           for prev_guess in self.guesses
                           for c, p, g in zip(self.correct, prev_guess, guess))

        return (length_ok()
                and letters_can_be_in_word()
                and correct_letters_respected()
                and hints_ok()
                and hint_positions_ok())

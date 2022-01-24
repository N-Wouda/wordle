import unittest

from src.classes import Wordle


class TestWordle(unittest.TestCase):

    def test_match_length(self):
        wordle = Wordle([], "", "*****")

        self.assertTrue(wordle.match("a" * 5))
        self.assertFalse(wordle.match("a" * 6))
        self.assertFalse(wordle.match("a" * 4))

    def test_match_letters_can_be_in_word(self):
        wordle = Wordle(["anode"], "", "*****")

        self.assertFalse(wordle.match("anode"))  # none of these are in the word
        self.assertTrue(wordle.match("risky"))  # but these could be

    def test_match_correct_letters_respected(self):
        wordle = Wordle(["anode"], "", "*no**")

        self.assertTrue(wordle.match("known"))
        self.assertFalse(wordle.match("risky"))
        self.assertFalse(wordle.match("anode"))

    def test_match_hints_ok(self):
        wordle = Wordle(["anode"], "oln", "*****")

        self.assertTrue(wordle.match("colon"))  # uses all the hints
        self.assertFalse(wordle.match("wonky"))  # does not use l

    def test_match_hint_positions_ok(self):
        wordle = Wordle(["colon"], "oln", "*****")

        self.assertTrue(wordle.match("knoll"))  # ok
        self.assertFalse(wordle.match("nobly"))  # o cannot be in 2nd position

    def test_match_issue_1(self):
        # See https://github.com/N-Wouda/wordle/issues/1
        wordle = Wordle(["pears", "humid", "colon"], "oln", "*****")

        self.assertTrue(wordle.match("klong"))
        self.assertFalse(wordle.match("flown"))
        self.assertFalse(wordle.match("xylon"))

    def test_match_raises_when_guess_is_not_alpha(self):
        wordle = Wordle([], "", "*****")

        with self.assertRaises(AssertionError):
            wordle.match("12345")

    def test_match_ignore_case(self):
        wordle = Wordle(["anode"], "", "*****")

        self.assertTrue(wordle.match("WITTY"))
        self.assertTrue(wordle.match("witty"))

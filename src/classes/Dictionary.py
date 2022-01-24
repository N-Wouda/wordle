class Dictionary:
    words: list[str]

    def __init__(self, loc: str):
        with open(loc, 'r') as fh:
            self.words = [word.strip().lower() for word in fh.readlines()]

    def __iter__(self):
        yield from self.words

    def __len__(self):
        return len(self.words)

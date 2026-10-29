from collections import defaultdict
from typing import List

class CountSquares:
    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        # Compile candidates
        candidates = set()

        for x, y in self.freq:
            if abs(x - px) == abs(y - py) and x != px:
                candidates.add((x, y))

        # Process candidates until none remain
        while candidates:
            x, y = candidates.pop()

            res += (
                self.freq[(x, y)]
                * self.freq.get((x, py), 0)
                * self.freq.get((px, y), 0)
            )

        return res